# coding: utf8

import time
import serial
from light_modbus.crc_mdb import *

port = 'COM23'
ser = serial.Serial(port, 9600, timeout=0.300)

# -- нарисовать форму
from Tkinter import *

root = Tk()

#  панель с органами управления
pn_left = Frame(root, width=900, bg='darkblue')
pn_left.pack(side='left', fill='y')

ed_width = 10
cl_contr = 'darkblue'
## заголовок блока состояния
lb_stathdr = Label(pn_left, text='Работа с modbus RTU:', bg=cl_contr, fg='white')
lb_stathdr.grid(row=0, column=0, columnspan=2)
row_num = 1

# заголовки:
lb_adr = Label(pn_left, text='Id устройства:', bg=cl_contr, fg='white')
lb_adr.grid(row=row_num, column=0, sticky=W, padx=10)

lb_cmd = Label(pn_left, text='команда:', bg=cl_contr, fg='white')
lb_cmd.grid(row=row_num, column=1, sticky=W, padx=10)

lb_adr = Label(pn_left, text='адрес регистра:', bg=cl_contr, fg='white')
lb_adr.grid(row=row_num, column=2, sticky=W, padx=10)

lb_count = Label(pn_left, text='число регистров:', bg=cl_contr, fg='white')
lb_count.grid(row=row_num, column=3, sticky=W, padx=10)

row_num += 1

## Id устройства
ed_id = Entry(pn_left, width=4)
ed_id.grid(row=row_num, column=0, sticky=W, padx=20)
## команда

ed_cmd = Entry(pn_left, width=ed_width)
ed_cmd.grid(row=row_num, column=1, sticky=W, padx=20)

## номер регистра
ed_adr = Entry(pn_left, width=ed_width)
ed_adr.grid(row=row_num, column=2, sticky=W, padx=20)

## количество регистров
ed_count = Entry(pn_left, width=ed_width)
ed_count.grid(row=row_num, column=3, sticky=W, padx=20)

row_num += 1


# = аккуратно извлечь число из поля
def get_bt(txt):
    tmps = "0000" + txt
    bt = int(tmps[-2:])
    return bt


# = разбить строку на 2 байта
def get_highlow(txt):
    tmps = "0000" + txt
    tmpl = int(tmps[-2:])
    tmph = int(tmps[-4:-2])
    return tmph, tmpl


send_arr = []  # - отправляемый массив


def fn_sendcmd(ev):
    global send_arr
    send_arr = []
    id = get_bt(ed_id.get())
    cmd = get_bt(ed_cmd.get())

    adrh, adrl = get_highlow(ed_adr.get())

    counth, countl = get_highlow(ed_count.get())

    send_arr.append(id)
    send_arr.append(cmd)
    send_arr.append(adrh)
    send_arr.append(adrl)

    vals = tx_vals.get("1.0", END)
    print vals
    ls_vals = vals.split('\n')
    print ls_vals
    len_vals = len(ls_vals) - 1  # каждая строка данных дть завершена <Enter>
    print len_vals

    # отработать разные по типу пакета команды отправки
    cmd_num = int(ed_cmd.get())
    if cmd_num > 0 and cmd_num < 5:
        send_arr.append(counth)
        send_arr.append(countl)
    elif cmd_num == 5 or cmd_num == 6:
        data = ls_vals[0]
        datah = int(data[0:2], 16)
        datal = int(data[2:4], 16)
        send_arr.append(datah)
        send_arr.append(datal)
    elif cmd_num == 15 or cmd_num == 16:
        send_arr.append(counth)
        send_arr.append(countl)
        # здесь число слов для битовой записи не равно числу битовых регистров
        send_arr.append(len_vals * 2)
        # print send_arr, '\n', len_vals
        for val_num in range(len_vals):
            data = ls_vals[val_num]
            datah, datal = get_highlow(str(data))
            send_arr.append(datah)
            send_arr.append(datal)
    else:
        print 'wrong command'

    tx_sect.insert(END, 'send: \n')

    # send_arr = [0x18, 0x04, 0x00, 0x33, 0x00, 0x01]
    # send_arr = [ 0x18, 0x10, 0x00, 0x32, 0x00, 0x01, 0x02, 0x00, 0x05]

    send_arr = addcrc(send_arr)
    for bt in send_arr:
        st = hex(256 + bt)
        tx_sect.insert(END, st[-2:] + ' ')
    tx_sect.insert(END, '\n')

    # отправить
    values = bytearray(send_arr)
    ser.write(values)

    ls_in = []

    ls_in = ser.read(200)

    if len(ls_in) < 1:
        answ = 'device not answer \n'
        tx_sect.insert(END, answ)
    else:
        tx_sect.insert(END, 'receive: \n')

        st = ''.join(["%02X " % ord(x) for x in ls_in])

        tx_sect.insert(END, st + '\n')

        # - проверить на контрольную сумму
        ls = [ord(bt) for bt in ls_in]
        # answ_crc = crc16bt(ls_in)
        answ_crc = crc16bt(ls)
        if answ_crc:
            tx_sect.insert(END, 'CRC - error: \n')
        else:
            tx_sect.insert(END, 'CRC - OK: \n')


bt_sendcmd = Button(pn_left, text=' отправить ')
bt_sendcmd.bind("<Button-1>", fn_sendcmd)
bt_sendcmd.grid(row=row_num, column=3, sticky=W, padx=20, pady=10)

lb_vals = Label(pn_left, text='значения \n регистров:', bg=cl_contr, fg='white')
lb_vals.grid(row=row_num, column=2, sticky=W, padx=10)

lb_cmds = Label(pn_left, text='список \n команд ', bg=cl_contr, fg='white')
lb_cmds.grid(row=row_num, column=1, sticky=W, padx=10)

row_num += 1

tx_vals = Text(pn_left, height=10, width=ed_width - 1)
tx_vals.grid(row=row_num, column=2, sticky=W, padx=20)

ls_cmds = [2, 1, 5, 15, 4, 3, 6, 16]


def fn_selcommand(ev):
    ed_cmd.delete(0, END)
    cmd_index = lx_cmds.curselection()[0]
    # print cmd_index
    cmd = ls_cmds[cmd_index]
    ed_cmd.insert(END, cmd)


lx_cmds = Listbox(pn_left, height=10, width=28)
lx_cmds.grid(row=row_num, column=1, sticky=W, padx=10)
lx_cmds.bind('<<ListboxSelect>>', fn_selcommand)
for cmd in ["read group Discrete Inputs(2)", "read group Coils(1)",
            "write single Coil(5)", "write group Coils(15)",
            "read group Input Registers(4)", "read group Holding Registers(3)",
            "write single Holding Register(6)", "write group Holding Registers(16)"]:
    lx_cmds.insert(END, cmd)

'''
'''

# -- правая панель для текста сектора
pn_right = Frame(root, width=300)
pn_right.pack(side='right', fill='both', expand=1)

##-- поле для вывода текста в правой панели
tx_sect = Text(pn_right, height=35, width=44)
tx_sect.grid(row=0, column=0)

sb_hor = Scrollbar(pn_right, command=tx_sect.xview, orient=HORIZONTAL)
sb_hor.grid(row=1, column=0, sticky=W + E + N + S)

sb_ver = Scrollbar(pn_right, command=tx_sect.yview, orient=VERTICAL)
sb_ver.grid(row=0, column=1, sticky=W + E + N + S)

tx_sect.config(yscrollcommand=sb_ver.set, xscrollcommand=sb_hor.set, wrap=NONE)

# -- запустить окно программы
root.mainloop()
