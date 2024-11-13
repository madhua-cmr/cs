def ones_complement(data):
    return ''.join('1' if bit == '0' else '0' for bit in data)
def check_sum(data,block_size):
    data = data.zfill(len(data) + block_size - len(data) % block_size)
    result = data[:block_size]
    for i in range(block_size,len(data),block_size):
        current_block = data[i:i + block_size]
        result = bin(int(result,2) + int(current_block,2))[2:]
        if len(result) > block_size:
            result = bin(int(result[-block_size:],2) + 1)[2:]
    result = result.zfill(block_size)
    return ones_complement(result)
def checker(sent_message,rec_message,block_size):
    return check_sum(sent_message+rec_message,block_size)
sent_message = input("")
rec_message = input("")
block_size = int(input(""))
print("no error" if checker(sent_message,rec_message,block_size) else "error")
