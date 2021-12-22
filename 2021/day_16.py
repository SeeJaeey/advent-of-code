from math import prod

input = """005410C99A9802DA00B43887138F72F4F652CC0159FE05E802B3A572DBBE5AA5F56F6B6A4600FCCAACEA9CE0E1002013A55389B064C0269813952F983595234002DA394615002A47E06C0125CF7B74FE00E6FC470D4C0129260B005E73FCDFC3A5B77BF2FB4E0009C27ECEF293824CC76902B3004F8017A999EC22770412BE2A1004E3DCDFA146D00020670B9C0129A8D79BB7E88926BA401BAD004892BBDEF20D253BE70C53CA5399AB648EBBAAF0BD402B95349201938264C7699C5A0592AF8001E3C09972A949AD4AE2CB3230AC37FC919801F2A7A402978002150E60BC6700043A23C618E20008644782F10C80262F005679A679BE733C3F3005BC01496F60865B39AF8A2478A04017DCBEAB32FA0055E6286D31430300AE7C7E79AE55324CA679F9002239992BC689A8D6FE084012AE73BDFE39EBF186738B33BD9FA91B14CB7785EC01CE4DCE1AE2DCFD7D23098A98411973E30052C012978F7DD089689ACD4A7A80CCEFEB9EC56880485951DB00400010D8A30CA1500021B0D625450700227A30A774B2600ACD56F981E580272AA3319ACC04C015C00AFA4616C63D4DFF289319A9DC401008650927B2232F70784AE0124D65A25FD3A34CC61A6449246986E300425AF873A00CD4401C8A90D60E8803D08A0DC673005E692B000DA85B268E4021D4E41C6802E49AB57D1ED1166AD5F47B4433005F401496867C2B3E7112C0050C20043A17C208B240087425871180C01985D07A22980273247801988803B08A2DC191006A2141289640133E80212C3D2C3F377B09900A53E00900021109623425100723DC6884D3B7CFE1D2C6036D180D053002880BC530025C00F700308096110021C00C001E44C00F001955805A62013D0400B400ED500307400949C00F92972B6BC3F47A96D21C5730047003770004323E44F8B80008441C8F51366F38F240"""

example1 = """8A004A801A8002F478"""

example2 = """620080001611562C8802118E34"""

example3 = """C0015000016115A2E0802F182340"""

example4 = """A0016C880162017C3686B18A3D4780"""

test = """38006F45291200"""

hex2bin = str.maketrans({
               "0":"0000","1":"0001","2":"0010","3":"0011",
               "4":"0100","5":"0101","6":"0110","7":"0111",
               "8":"1000", "9":"1001","A":"1010","B":"1011",
               "C":"1100", "D":"1101", "E":"1110","F":"1111"})

transmission = input.translate(hex2bin)
versions = 0

def decode_cmd(data, i, val):
    length = packets = 0
    if data[i] == '0':
        length = int(data[i+1:i+16], 2)
        commands, i = decode_length(data, i + 16, length)
    else:
        packets = int(data[i+1:i+12], 2)
        commands, i = decode_count(data, i + 12, packets)
    if val == 0: return sum(commands), i
    if val == 1: return prod(commands), i
    if val == 2: return min(commands), i
    if val == 3: return max(commands), i
    if val == 5: return int(commands[0] > commands[1]), i
    if val == 6: return int(commands[0] < commands[1]), i
    if val == 7: return int(commands[0] == commands[1]), i

def decode(data,i=0):
    global versions
    versions += int(data[i:i+3], 2)
    type_id = int(data[i+3:i+6], 2)
    if type_id == 4: return decode_keys(data, i + 6)
    else: return decode_cmd(data, i + 6, type_id)

def decode_keys(data, i):
    value = ''
    while True:
        value += data[i+1:i+5]
        if data[i] == '0':
            return int(value, 2), i + 5
        i += 5

def decode_length(data, i, length):
    end = i + length
    values = []
    while i < end:
        value, i = decode(data, i)
        values.append(value)
    return values, i

def decode_count(data, i, count):
    packets = 0
    values = []
    while packets < count:
        value, i = decode(data, i)
        values.append(value)
        packets += 1
    return values, i

print("Part 2:", decode(transmission)[0])
print("Part 1:", versions)