import chardet

def decode_leb128(data):
    result = []
    idx = 0
    while idx < len(data):
        value = 0
        shift = 0
        while True:
            byte = data[idx]
            idx += 1
            value |= (byte & 0x7f) << shift
            shift += 7
            if byte & 0x80 == 0:
                break
        result.append(value)
    return result
    
def integers_to_text(integers):
    text = ''.join(chr(i) for i in integers if i <= 0x10FFFF)
    return text

with open('data/repo_THE_OG.car', 'rb') as f:
    raw_data =f.read()

integers = decode_leb128(raw_data)
text = integers_to_text(integers)
print(text)




"""
int_data = decode_leb128(raw_data)
text = ''.join(int_data).decode('utf-8',errors='ignore')
print(text)

    result = chardet.detect(raw_data)
    print(result['encoding'])

try:
    decoded_data = raw_data.decode('ULEB128', errors='ignore')
    print(decoded_data)
except UnicodeDecodeError:
    print("Failed to decode")"""
