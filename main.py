from pymodbus.client.sync import ModbusTcpClient

host = '192.168.88.110' #ip address sleve plc
port = 502 #port modbus untuk ke plc

client = ModbusTcpClient(host, port) #inisial client
client.connect() #konekin ke klien / sleve

client.write_register(101, 90) #write value 90 ke register 101
client.write_register(102, 48) #write value 48 ke register 102
client.write_register(103, 0) # write value 103 ke register 103

rr = client.read_holding_registers(0x65, 3, unit=0) #baca register(register dalam HexaDesimal, panjang range register n-indeks)
assert(rr.function_code < 0x80)                     #test that we are not an error
print(rr)
print(rr.registers)



