import random
import struct
from ModbusclientCMD import ModbusGenerateCMD




class ModbusTCP(ModbusGenerateCMD):
    def __init__(self, slave_id, cmd, register_number, number_of_regs, data):
        ModbusGenerateCMD.__init__(self, slave_id, cmd, register_number, number_of_regs, data)

    def read_group_Discrete_Inputs(self, register_number, number_of_regs=1):
        """
        :read_group_Discrete_Inputs
        """
        send_mas = ModbusGenerateCMD.pre_read_group_Discrete_Inputs(register_number,
                                                                    number_of_regs
                                                                    )
        f_body = struct.pack('B', fc) + body

        # build frame ModBus Application Protocol header (mbap)
        self.__hd_tr_id = random.randint(0, 65535)
        tx_hd_pr_id = 0
        tx_hd_length = len(f_body) + 1
        f_mbap = struct.pack('>HHHB', self.__hd_tr_id, tx_hd_pr_id,
                             tx_hd_length, self.__unit_id)

        return f_mbap + send_mas

    def read_group_Coils(self, register_number, number_of_regs=1):
        """
        :cmd = 1
        """
        send_mas = ModbusGenerateCMD.pre_read_group_Coils(register_number,
                                                          number_of_regs
                                                          )
        return send_mas

    def read_group_Input_Registers(self, register_number, number_of_regs=1):
        """
        :cmd = 4
        """
        send_mas = ModbusGenerateCMD.pre_read_group_Input_Registers(register_number,
                                                                    number_of_regs
                                                                    )
        return send_mas

    def read_group_Holding_Registers(self, register_number, number_of_regs=1):
        """
        :cmd = 3
        """
        send_mas = ModbusGenerateCMD.pre_read_group_Holding_Registers(register_number,
                                                                      number_of_regs
                                                                      )
        return send_mas

    def write_group_Coils(self, register_number, number_of_regs=1, data=None):
        """
        :cmd = 15
        """
        send_mas = ModbusGenerateCMD.pre_write_group_Coils(register_number,
                                                           number_of_regs,
                                                           data
                                                           )
        return send_mas

    def write_single_Holding_Register(self, register_number, number_of_regs=1, data=None):
        """
        :cmd = 6
        """
        send_mas = ModbusGenerateCMD.pre_write_single_Holding_Register(register_number,
                                                                       number_of_regs,
                                                                       data
                                                                       )
        return send_mas

    def write_group_Holding_Registers(self, register_number, number_of_regs=1, data=None):
        """
        :cmd = 16
        """
        send_mas = ModbusGenerateCMD.pre_write_group_Holding_Registers(register_number,
                                                                       number_of_regs,
                                                                       data
                                                                       )
        return send_mas