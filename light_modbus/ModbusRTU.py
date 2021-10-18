from .ModbusclientCMD import *
from .crc_mdb import addcrc


class ModbusRtuClient:
    '''
    Modbus generate commands: make commands
    '''

    def __init__(self, slave_id):
        self.slave_id = slave_id
        self.pointer = ModbusGenerateCMD()

    def read_group_Discrete_Inputs(self, register_number, number_of_regs=1):
        """
        :read_group_Discrete_Inputs
        """
        send_mas = self.pointer.pre_read_group_Discrete_Inputs(register_number,
                                                               number_of_regs
                                                               )
        send_mas.insert(0, self.slave_id)
        return addcrc(send_mas)

    def read_group_Coils(self, register_number, number_of_regs=1):
        """
        :cmd = 1
        """
        send_mas = self.pointer.pre_read_group_Coils(register_number,
                                                     number_of_regs
                                                     )
        send_mas.insert(0, self.slave_id)
        return addcrc(send_mas)

    def read_group_Input_Registers(self, register_number, number_of_regs=1):
        """
        :cmd = 4
        """
        send_mas = self.pointer.pre_read_group_Input_Registers(register_number,
                                                               number_of_regs
                                                               )
        send_mas.insert(0, self.slave_id)
        return addcrc(send_mas)

    def read_group_Holding_Registers(self, register_number, number_of_regs=1):
        """
        :cmd = 3
        """
        send_mas = self.pointer.pre_read_group_Holding_Registers(register_number,
                                                                 number_of_regs
                                                                 )
        send_mas.insert(0, self.slave_id)
        return addcrc(send_mas)

    def write_group_Coils(self, register_number, number_of_regs=1, data=None):
        """
        :cmd = 15
        """
        send_mas = self.pointer.pre_write_group_Coils(register_number,
                                                      number_of_regs,
                                                      data
                                                      )
        send_mas.insert(0, self.slave_id)
        return addcrc(send_mas)

    def write_single_Holding_Register(self, register_number, number_of_regs=1, data=None):
        """
        :cmd = 6
        """
        send_mas = self.pointer.pre_write_single_Holding_Register(register_number,
                                                                  number_of_regs,
                                                                  data
                                                                  )
        send_mas.insert(0, self.slave_id)
        return addcrc(send_mas)

    def write_group_Holding_Registers(self, register_number, number_of_regs=1, data=None):
        """
        :cmd = 16
        """
        send_mas = self.pointer.pre_write_group_Holding_Registers(register_number,
                                                                  number_of_regs,
                                                                  data
                                                                  )
        send_mas.insert(0, self.slave_id)
        return addcrc(send_mas)
