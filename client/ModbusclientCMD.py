# coding: utf8

from .pdu import ModbusPDU
from . import (READ_GROUP_DISCRETE_COILS,
               READ_GROUP_COILS,
               READ_GROUP_INPUT_REGISTERS,
               READ_GROUP_HOLDING_REGISTERS,
               WRITE_GROUP_COILS,
               WRITE_SINGLE_HOLDING_REGISTERS,
               WRITE_GROUP_HOLDING_REGISTERS)



class ModbusGenerateCMD(ModbusPDU):
    '''
    Modbus generate commands: make commands
    '''
    def __init__(self, slave_id, cmd, register_number, number_of_regs, data):
        ModbusPDU.__init__(self, cmd, register_number, number_of_regs, data)
        self.slave_id = slave_id

    def pre_read_group_Discrete_Inputs(self, register_number, number_of_regs=1):
        """
        :read_group_Discrete_Inputs
        """
        command = ModbusPDU(
            cmd=READ_GROUP_DISCRETE_COILS,
            register_number=register_number,
            number_of_regs=number_of_regs,
            data=None
        )
        mas = command.pdu(self)
        mas.insert(0, self.slave_id)
        return mas

    def pre_read_group_Coils(self, register_number, number_of_regs=1):
        """
        :cmd = 1
        """
        command = ModbusPDU(
                            READ_GROUP_COILS,
                            register_number=register_number,
                            number_of_regs=number_of_regs,
                            data=None
                            )
        mas = command.pdu(self)
        mas.insert(0, self.slave_id)
        return mas

    def pre_read_group_Input_Registers(self, register_number, number_of_regs=1):
        """
        :cmd = 4
        """
        command = ModbusPDU(
            cmd=READ_GROUP_INPUT_REGISTERS,
            register_number=register_number,
            number_of_regs=number_of_regs,
            data=None
        )
        mas = command.pdu(self)
        mas.insert(0, self.slave_id)
        return mas

    def pre_read_group_Holding_Registers(self, register_number, number_of_regs=1):
        """
            :cmd = 3
            """
        command = ModbusPDU(
            cmd=READ_GROUP_HOLDING_REGISTERS,
            register_number=register_number,
            number_of_regs=number_of_regs,
            data=None
        )
        mas = command.pdu(self)
        mas.insert(0, self.slave_id)
        return mas

    def pre_write_group_Coils(self, register_number, number_of_regs=1, data=None):
        """
        :cmd = 15
        """
        command = ModbusPDU(
            cmd=WRITE_GROUP_COILS,
            register_number=register_number,
            number_of_regs=number_of_regs,
            data=data
        )
        mas = command.pdu(self)
        mas.insert(0, self.slave_id)
        return mas

    def pre_write_single_Holding_Register(self, register_number, number_of_regs=1, data=None):
        """
        :cmd = 6
        """
        command = ModbusPDU(
            cmd=WRITE_SINGLE_HOLDING_REGISTERS,
            register_number=register_number,
            number_of_regs=number_of_regs,
            data=data
        )
        mas = command.pdu(self)
        mas.insert(0, self.slave_id)
        return mas

    def pre_write_group_Holding_Registers(self, register_number, number_of_regs=1, data=None):
        """
        :cmd = 16
        """
        command = ModbusPDU(
            cmd=WRITE_GROUP_HOLDING_REGISTERS,
            register_number=register_number,
            number_of_regs=number_of_regs,
            data=data
        )
        mas = command.pdu(self)
        mas.insert(0, self.slave_id)
        return mas


