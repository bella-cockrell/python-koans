#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Duck:
    @property
    def name(self):
        return "Donald"
    
    @property
    def sound(self):
        return "quack"
    
    def feet(self):
        return 2