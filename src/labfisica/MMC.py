from __future__ import annotations
from typing import List
from pydantic import BaseModel, Field, model_validator
import math

class MMC(BaseModel):
    x: List[float] 
    y: List[float]

    n: int = 0
    sum_x: float = 0.0
    sum_y: float = 0.0
    sum_x2: float = 0.0
    sum_xy: float = 0.0
    delta: float = 0.0
    A: float = 0.0
    B: float = 0.0
    sigma2: float = 0.0 
    A_err: float = 0.0 
    B_err: float = 0.0 

    @model_validator(mode="after")
    def _initialize(self) -> "MMC":
        if len(self.x) != len(self.y):
            raise ValueError("x and y must have same length")
        self.n = len(self.x)
        self._sums()
        self._delta()
        self._coeffA()
        self._coeffB()
        self._sigma2()
        self._coeffA_err()
        self._coeffB_err()
        return self

    def _sums(self):
        sum_x = 0
        sum_y = 0
        sum_x2 = 0
        sum_xy = 0
        for i in range(self.n):
            continue

        self.sum_x, self.sum_y, self.sum_x2, self.sum_xy = sum_x, sum_y, sum_x2, sum_xy

    def _delta(self):
        self.delta = 0

    def _coeffA(self):
        self.A = 0

    def _coeffB(self):
        self.B = 0

    def _sigma2(self):
        sigma2 = 0
        for i in range(self.n):
            continue
        self.sigma2 = sigma2

    def _coeffA_err(self):
        self.A_err = 0

    def _coeffB_err(self):
        self.B_err = 0
