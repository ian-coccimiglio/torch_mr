#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 03:37:22 2024

@author: ian
"""
import torch


class TorchMemoryReport:

    @classmethod
    def get_total_memory(cls):
        if torch.cuda.is_available():
            return torch.cuda.mem_get_info()[1] / (1 << 30)
        else:
            raise RuntimeError("CUDA is not available")

    GB = "GB"
    COLORS = {
        "green": "\x1b[1;32m",
        "yellow": "\x1b[1;33m",
        "red": "\x1b[1;31m",
        "gray": "\x1b[1;30m",
        "end": "\x1b[0m",
    }
    GB_conversion = 1 << 30

    @classmethod
    def ascii_bar(cls, current, capacity):
        total_cubes = 24
        empty_amount = int(total_cubes * current / capacity)
        filled_amount = total_cubes - empty_amount
        if filled_amount <= 8:
            color = cls.COLORS["green"]
        elif (filled_amount > 8) and (filled_amount <= 16):
            color = cls.COLORS["yellow"]
        elif filled_amount > 16:
            color = cls.COLORS["red"]
        filled_cubes = filled_amount * (color + "▮" + cls.COLORS["end"])
        empty_cubes = empty_amount * (
            cls.COLORS["gray"] + "▮" + cls.COLORS["end"]
        )
        return filled_cubes + empty_cubes

    @classmethod
    def print_vram(cls, total_memory):
        free_memory = torch.cuda.mem_get_info()[0] / cls.GB_conversion
        bar = cls.ascii_bar(free_memory, total_memory)
        print(
            f"{'VRAM:':<10} {total_memory - free_memory:<5.2f}/{total_memory:.2f}{cls.GB:<10} {bar:^10}"
        )

    @classmethod
    def print_reserved(cls, total_memory):
        reserved_memory = torch.cuda.memory_reserved() / cls.GB_conversion
        unreserved = total_memory - reserved_memory
        bar = cls.ascii_bar(unreserved, total_memory)
        print(
            f"{'Reserved:':<10} {reserved_memory:<5.2f}/{total_memory:.2f}{cls.GB:<10} {bar:^10}"
        )

    @classmethod
    def print_allocated(cls, total_memory):
        allocated_memory = torch.cuda.memory_allocated() / cls.GB_conversion
        unallocated = total_memory - allocated_memory
        bar = cls.ascii_bar(unallocated, total_memory)
        print(
            f"{'Allocated:':<10} {allocated_memory:<5.2f}/{total_memory:.2f}{cls.GB:<10} {bar:^10}"
        )

    @classmethod
    def print_all(cls):
        try:
            total_memory = cls.get_total_memory()
            cls.print_vram(total_memory)
            cls.print_reserved(total_memory)
            cls.print_allocated(total_memory)
        except RuntimeError as e:
            print(e)

    @staticmethod
    def clear_torch_cache():
        torch.cuda.empty_cache()


TorchMemoryReport.print_all()
