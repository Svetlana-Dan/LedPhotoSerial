import serial
import time 

lengths = {'f': 3,
           'u': 0,
           'd': 0,
           'a': 3, 
           'b': 0}
           
def get_connection(port): //подключение
    ser = serial.Serial(port, timeout = 1)
    return ser

def send(ser, message, mesg_len): //отправляет команды в ардуино
    ser.write(message) 
    time.sleep(0.1) //задержка
    result = None 
    if mesg_len != 0:
        data = ser.read(mesg_len) //считывает сообщение
        result = data.decode() //декодирует
        result = result.strip() //удаляем пробелы
        print(result)
    return result
   
val_max = 0
val_min = 1024
lst = []
stop = False

if __name__ == '__main__':
    ser = get_connection("/dev/cu.usbserial-1130") //подключаемся
    while True:
          while stop: //чтобы пока не считал не работало
            timeout = time.time() + 10 //текущее время +10с
            cmd = 'f' 
            val = send(ser, cmd.encode(), lengths[cmd]) // получаем значения
            if val: //если зачение пришло
                val = int(val) //записываем значение в инт
                lst.append(val) //добавляем значение в массив??
                if val > val_max:
                    val_max = val //находим максимум
                if val < val_min:
                    val_min = val //находим минимум
                if val < ((val_min + val_max) / 2):
                    send(ser, 'u'.encode(), 0) //вкл
                else:
                    send(ser, 'd'.encode(), 0) //выкл
                time.sleep(1)
            if (time.time() > timeout): //если прошло 10с прерывается
                break
        inp = input("Enter command:") //считываем команду
        lenght = lenghts.get(inp, 0) //записываем длину команды
        send(ser, inp.encode(), lenght) //отправляем в ардуино
        if inp == 'a':
            stop = True
        if inp == 'b':
            stop = False
