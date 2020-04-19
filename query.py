# https://github.com/RealAtom/easy-samp-query

import socket

def encode_bytes(*args):
    ByteResult = b''
    for arg in args:
        if isinstance(arg, bytes):
            ByteResult += arg
        elif isinstance(arg, str):
            ByteResult += bytes(arg)
        elif isinstance(arg, int):
            ByteResult += bytes([arg])
    return ByteResult

def MakeQueryPayload(server_ip, server_port, opcode):
    TargetAddress = encode_bytes(*[(int(n)) for n in server_ip.split('.')])
    TargetPort = encode_bytes(int(server_port) & 0xFF, int(server_port) >> 8 & 0xFF)

    Payload = b'SAMP' \
            + TargetAddress \
            + TargetPort \
            + opcode.encode() \
            + b''
    return Payload

def SendQueryRequest(address, port, opcode):
    try:
        address = socket.gethostbyname(address)

        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.settimeout(1)

        payload = MakeQueryPayload(address, port, opcode)
        sock.sendto(payload, (address, int(port)))

        data = sock.recv(4096)
        response = data[11:]

        sock.close()
        return response

    except socket.error:
        return False
