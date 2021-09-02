from pymodbus.client.sync import ModbusTcpClient

host = '192.168.88.110' #ip address plc
port = 502 #port modbus untuk ke plc

client = ModbusTcpClient(host, port) #inisial client
client.connect() #konekin ke klien

x = 0

while True :
    if x == 0:
        x = 1
        client.write_register(101, x)  # nge write value 1 ke register 101
    elif x == 1:
        x = 0
        client.write_register(101, x)  # nge write value 1 ke register 101

    rr = client.read_holding_registers(0x65, 1, unit=0)  # baca register(register, panjang)
    assert (rr.function_code < 0x80)  # test that we are not an error
    print(rr)
    print(rr.registers)