****
**Modbus** — протокол, работающий по принципу «клиент-сервер».  
Широко применяется в промышленности.  
**Modbus** может использоваться для передачи данных через последовательные линии связи
RS-485, RS-422, RS-232, а также сети TCP/IP.    
**Отправка запроса осуществляется по команде:**  
**Запрос:**  
![Alt-текст](http://we.easyelectronics.ru/uploads/images/00/26/61/2013/10/25/06d0aa.png "!")  
**Ответ:**   
![Alt-текст](http://we.easyelectronics.ru/uploads/images/00/26/61/2013/10/25/7d1b91.jpg "#")  
[_ID_] - Адрес ведомого устройства. Диапазон 1 до 247;   
[_КОМАНДА_] - команда чтения/записи;  
[_АДРЕС ДАННЫХ_] - адреса регистра для чтения;  
[_КОЛИЧЕСТВО_] - чило выходных регистров;  
[_CRC_] - контрольная сумма.  

Подробнее по [ссылке](https://www.sites.google.com/site/fieldbusbook/seti/modbus-rtu-ascii-rus).

****
**Работа с библиотекой**  
Скачать библиотеку:  

`https://github.com/rpopov94/PyModbus.git`  


___Технические требования___

* Библиотека задумана кроссплатформенной
* `python==3.8`

****

**Установка зависимостей:**  

`pip install serial`  

****

**Осуществление запроса**  

1. Подключиться к com - порту;  
`connect_to_port(name, baudrate=None, bytesize=None, parity=None, stopbits=None, timeout=1)`  
  _name_  - имя порта;  
  _baudrate_ - скорость обмена данными;  
  _bytesize_ - длина слова данных  
  _parity_ - паритет;  
  _stopbits_ - Количетсво стоп бит;
  _timeout_ - задержка ответа (сек);  
2. Команда:

Осуществление запроса осуществляется с помощью функции:
  
`fn_sendcmd(id, cmd, register_number, number_of_regs, *args)`
- id -базовый адрес устройства;  
- cmd - команда чтения/записи;
- register_number - номер регистра для наблючения;
- number_of_regs - число регистров на вывод;     
- *args  - дополнительные параметры.

_Если запрос будет корретным, от утсройство вернёт ответ_  

Реализованы также более высокоуровневые функции, обеспечивающие доступ к данным из устройств:  
Группа функции для чтения:  
`read_group_Discrete_Inputs(id, register_number, number_of_regs=1)`
    
`read_group_Coils(id, register_number, number_of_regs=1)`

`read_group_Input_Registers(id, register_number, number_of_regs=1)`

`read_group_Holding_Registers(id, register_number, number_of_regs=1)`

Группа функции для записи:  

`write_group_Coils(id, register_number, number_of_regs=1, *args)`

`write_single_Holding_Register(id, register_number, number_of_regs=1, *args)`

`write_group_Holding_Registers(id, register_number, number_of_regs=1, *args)`

_Параметры_

`id` - базовый адрес устройства;  
`register_number` - номер регистра для наблючения;  
`number_of_regs` - число регистров на вывод;  
`*args `- сюда указываются данные для записи.  

3. Отключение от порта  
`ch_disconnect()`
 
*****    
**Основные регистры для работы**

* (0x02) — чтение значений из нескольких дискретных входов (Read Discrete Inputs);
* (0x03) — чтение значений из нескольких регистров хранения (Read Holding Registers);
* (0x04) — чтение значений из нескольких регистров ввода (Read Input Registers);
* (0x05) — запись значения одного флага (Force Single Coil);
* (0x06) — запись значения в один регистр хранения (Preset Single Register);
* (0x07) — Чтение сигналов состояния (Read Exception Status);
* (0x0F) — запись значений в несколько регистров флагов (Force Multiple Coils);
* (0x10) — запись значений в несколько регистров хранения (Preset Multiple Registers);
* (0x16) — запись в один регистр хранения с использованием маски «И» и маски «ИЛИ» (Mask Write Register);
* (0x18) — Чтение данных из очереди (Read FIFO Queue);
* (0x14) — Чтение из файла (Read File Record);
* (0x15) — Запись в файл (Write File Record);
* (0x08) — Диагностика (Diagnostic);
* (0x0B) — Чтение счетчика событий (Get Com Event Counter);
* (0x0C) — Чтение журнала событий (Get Com Event Log);
* (0x11) — Чтение информации об устройстве (Report Slave ID);
* (0x2B) — Encapsulated Interface Transport.
