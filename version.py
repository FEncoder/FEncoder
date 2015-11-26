# -*- coding: utf-8 -*-

from zlib import crc32


def version_info():
    return (0, 2, 0, 'R2', 'r23', '32-bit')


def version_serial():
    version = version_info()
    checksum = crc32('{major}.{minor}.{micro}.{revision} {machine}'.format(major=str(version[0]),
                                                                           minor=str(version[1]),
                                                                           micro=str(version[2]),
                                                                           revision=version[4][1:],
                                                                           machine=version[5]).encode())
    CRC = hex(checksum)[2:].upper()
    if len(CRC) == 8:
        return CRC
    elif len(CRC) < 8 and len(CRC) > 0:
        zeros = ['0' for _ in range(8-len(CRC))]
        return '{0}{1}'.format(''.join(zeros), CRC)
    else:
        return 'FFFFFFFF'
