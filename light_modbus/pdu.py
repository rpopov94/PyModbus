#coding: utf8

class ModbusPDU:

    '''Protocol data unit'''

    def __init__(self, cmd, register_number, number_of_regs, data):
        """
        :param cmd: Modbus function read/write
        :param register_number:
        :param number_of_regs:
        """
        self.cmd = cmd
        self.register_number = register_number
        self.number_of_regs = number_of_regs
        self.data = data

    def get_bt(self, txt):
        """
        :param txt: value
        :return: bit
        """
        tmps = "0000" + str(txt)
        bt = int(tmps[-2:])
        return bt

    def get_highlow(self, txt):
        """
        :param txt: register_number, number_of_regs
        :return: (high, low) value
        """
        tmps = "0000" + str(txt)
        tmpl = int(tmps[-2:])
        tmph = int(tmps[-4:-2])
        return tmph, tmpl

    def pdu(self, *args):
        '''
        :param cmd: Modbus function read/write
        :param register_number: register for read/write
        :param number_of_regs: number for read/write
        :param data: data for read/write
        :return: protocol data unit
        '''
        pdu_mas = []
        adrh, adrl = self.get_highlow(self.register_number)
        counth, countl = self.get_highlow(self.number_of_regs)
        datah, datal = None, None
        vals = None
        len_vals = 0
        if self.data is not None:
            datah, datal = self.get_highlow(self.data)
            vals = list(args)
            len_vals = len(vals)
        pdu_mas.append(self.cmd)
        pdu_mas.append(adrh)
        pdu_mas.append(adrl)
        if 0 < self.cmd < 5:
            pdu_mas.append(counth)
            pdu_mas.append(countl)
        elif self.cmd == 5 or self.cmd == 6:
            pdu_mas.append(datah)
            pdu_mas.append(datal)
        elif self.cmd == 15 or self.cmd == 16:
            pdu_mas.append(counth)
            pdu_mas.append(countl)
            pdu_mas.append(len_vals * 2)
            for i in range(len_vals):
                value = vals[i]
                datah, datal = self.get_highlow(value)
                pdu_mas.append(datah)
                pdu_mas.append(datal)

        return pdu_mas
