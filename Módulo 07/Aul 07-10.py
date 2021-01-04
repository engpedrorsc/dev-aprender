from abc import ABC, abstractmethod


class Monitor(ABC):
    @abstractmethod
    def aumentar_claridade(self, niveis):
        pass

    @abstractmethod
    def reduzir_claridade(self, niveis):
        pass


class MonitorFullHD(Monitor):
    def aumentar_claridade(self, niveis):
        return print(f'Aumentando a claridade em {niveis} pontos.')

    def reduzir_claridade(self, niveis):
        return print(f'Reduzindo a claridade em {niveis} pontos.')


monitor = MonitorFullHD()
monitor.aumentar_claridade(5)
monitor.reduzir_claridade(5)
