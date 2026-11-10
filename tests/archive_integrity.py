"""Validate the exact contents of a downloadable toolkit archive."""
import hashlib
import json


def verify_archive(archive, root):
    prefix = 'AI-ML-Engineering-Portfolio/'
    manifest_path = 'downloads/toolkit-manifest.json'
    manifest_bytes = (root / manifest_path).read_bytes()
    manifest = json.loads(manifest_bytes)
    names = archive.namelist()
    expected = {prefix + path for path in manifest} | {prefix + manifest_path}
    if len(names) != len(set(names)):
        raise ValueError('Toolkit contains duplicate archive members')
    if set(names) != expected:
        raise ValueError('Toolkit members do not exactly match the manifest')
    if archive.testzip() is not None:
        raise ValueError('Toolkit failed its ZIP checksum check')
    if archive.read(prefix + manifest_path) != manifest_bytes:
        raise ValueError('Archived manifest differs from the published manifest')
    for path, record in manifest.items():
        content = (root / path).read_bytes()
        if (hashlib.sha256(content).hexdigest() != record['sha256']
                or len(content) != record['bytes']):
            raise ValueError(f'Published file differs from its manifest record: {path}')
        if archive.read(prefix + path) != content:
            raise ValueError(f'Archived file differs from the published file: {path}')
