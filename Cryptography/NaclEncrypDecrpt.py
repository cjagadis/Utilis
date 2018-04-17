#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import nacl.secret
import nacl.utils
import base64
from pyblake2 import blake2b
import getpass


print("### ENCRYPTION")

# Fill password input into a blake2b key
# and use 32 byte as Salsa20 key
key = blake2b(digest_size=16)
key.update(getpass.getpass("PASSWORD:"))
key = key.hexdigest()

print("key: %s") % key


# This is your safe, you can use it to encrypt or decrypt messages
box = nacl.secret.SecretBox(key)

# This is our message to send, it must be a bytestring as SecretBox will
#   treat is as just a binary blob of data.
msg = b"whohdkreouncoeureoi98"
print("msg: %s")% msg

# This is a nonce, it *MUST* only be used once, but it is not considered
#   secret and can be transmitted or stored alongside the ciphertext. A
#   good source of nonce is just 24 random bytes.
nonce = nacl.utils.random(nacl.secret.SecretBox.NONCE_SIZE)
print("nonce: %s")% nacl.encoding.HexEncoder.encode(nonce)

# Encrypt our message, it will be exactly 40 bytes longer than the original
#   message as it stores authentication information and nonce alongside it.
encrypted = box.encrypt(msg, nonce, encoder=nacl.encoding.HexEncoder)

print("cipher: %s ")% encrypted

print("### DECRYPTION")

# new blake2b hash
key = blake2b(digest_size=16)
key.update(getpass.getpass("PASSWORD:"))
key = key.hexdigest()

# just to be safe its really empty and not reused
#   to demonstrate nonce is really not required for decryption
nonce = None
print("nonce: %s")% nonce

print("key: %s")% key

# init box with key
box = nacl.secret.SecretBox(key)

# for readability reasons, write enc content into msg var
msg = encrypted
print("msg: %s")% msg

# fun part. Only msg being used in box that was initialized only with the key
plain = box.decrypt(ciphertext=msg,encoder=nacl.encoding.HexEncoder)
print("plain: %s")% plain
