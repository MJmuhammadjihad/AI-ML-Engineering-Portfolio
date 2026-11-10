"""Exercise the release guard against independently corrupted ZIP packages."""
import hashlib
import io
import json
from pathlib import Path
import tempfile
import unittest
import warnings
import zipfile

from archive_integrity import verify_archive


class ArchiveIntegrityTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.root = Path(self.directory.name)
        (self.root / 'downloads').mkdir()
        payload = b'An original offline guide.\n'
        (self.root / 'guide.html').write_bytes(payload)
        manifest = json.dumps({'guide.html': {
            'bytes': len(payload), 'sha256': hashlib.sha256(payload).hexdigest()
        }}).encode()
        (self.root / 'downloads/toolkit-manifest.json').write_bytes(manifest)
        self.members = [
            ('AI-ML-Engineering-Portfolio/guide.html', payload),
            ('AI-ML-Engineering-Portfolio/downloads/toolkit-manifest.json', manifest)
        ]

    def verify(self, members):
        buffer = io.BytesIO()
        with warnings.catch_warnings():
            warnings.simplefilter('ignore', UserWarning)  # Deliberate duplicate fixture.
            with zipfile.ZipFile(buffer, 'w') as archive:
                for name, content in members:
                    archive.writestr(name, content)
        buffer.seek(0)
        with zipfile.ZipFile(buffer) as archive:
            verify_archive(archive, self.root)

    def test_valid_archive_passes(self):
        self.verify(self.members)

    def test_unlisted_file_is_rejected(self):
        with self.assertRaisesRegex(ValueError, 'exactly match'):
            self.verify(self.members + [('AI-ML-Engineering-Portfolio/extra.py', b'extra')])

    def test_missing_file_is_rejected(self):
        with self.assertRaisesRegex(ValueError, 'exactly match'):
            self.verify(self.members[1:])

    def test_duplicate_file_is_rejected(self):
        with self.assertRaisesRegex(ValueError, 'duplicate'):
            self.verify(self.members + [self.members[0]])

    def test_replaced_embedded_manifest_is_rejected(self):
        with self.assertRaisesRegex(ValueError, 'Archived manifest'):
            self.verify([self.members[0], (self.members[1][0], b'{}')])

    def test_changed_archived_payload_is_rejected(self):
        with self.assertRaisesRegex(ValueError, 'Archived file'):
            self.verify([(self.members[0][0], b'changed'), self.members[1]])

    def test_changed_published_payload_is_rejected(self):
        (self.root / 'guide.html').write_bytes(b'changed')
        with self.assertRaisesRegex(ValueError, 'manifest record'):
            self.verify(self.members)


if __name__ == '__main__':
    unittest.main()
