from abc import ABCMeta, abstractmethod
import time

class Platform(metaclass=ABCMeta):
	@abstractmethod
	def stop_systems(self):
		raise NotImplementedError('Please implement the method <stop_systems>!')

	@abstractmethod
	def start_systems(self):
		raise NotImplementedError('Please implement the method <start_systems>!')		

	@abstractmethod
	def heath_check_systems(self):
		raise NotImplementedError('Please implement the method <heath_check_systems>!')


class WebServer(Platform):
	__nodes = ['web_node_a','web_node_b','web_node_c']
	def stop_systems(self):
		for system in self.__nodes:
			print("Stopping system: {}".format(system))
			time.sleep(0.5)

	def start_systems(self):
		for system in self.__nodes:
			print("Starting system: {}".format(system))
			time.sleep(0.5)

	def heath_check_systems(self):
		for system in self.__nodes:
			print("Checking system: {}".format(system))
			time.sleep(0.5)

class Firewall(Platform):
	__nodes = ['fw_node_a','fw_node_b','fw_node_c']
	def stop_systems(self):
		for system in self.__nodes:
			print("Stopping system: {}".format(system))
			time.sleep(0.5)

	def start_systems(self):
		for system in self.__nodes:
			print("Starting system: {}".format(system))
			time.sleep(0.5)

	def heath_check_systems(self):
		for system in self.__nodes:
			print("Checking system: {}".format(system))
			time.sleep(0.5)

class AppServer(Platform):
	__nodes = ['jvm_node_a','jvm_node_b','jvm_node_c']
	def stop_systems(self):
		for system in self.__nodes:
			print("Stopping system: {}".format(system))
			time.sleep(0.5)

	def start_systems(self):
		for system in self.__nodes:
			print("Starting system: {}".format(system))
			time.sleep(0.5)

	def heath_check_systems(self):
		for system in self.__nodes:
			print("Checking system: {}".format(system))
			time.sleep(0.5)

class PatchingFactory(object):
	def stop_all(self, platform_object):
		print('Stopping platfrom: {}'.format(platform_object))
		return eval(platform_object)().stop_systems()

	def start_all(self, platform_object):
		print('Starting platfrom: {}'.format(platform_object))
		return eval(platform_object)().start_systems()		

	def hc_all(self, platform_object):
		print('Checking platfrom: {}'.format(platform_object))
		return eval(platform_object)().heath_check_systems()

	def make_magic_happen(self,platform_object):
		self.hc_all(platform_object)
		self.stop_all(platform_object)
		self.start_all(platform_object)
		self.hc_all(platform_object)

PF = PatchingFactory()
PFORMS = ['WebServer','AppServer','Firewall']
for platform_to_stop in PFORMS:
	PF.hc_all(platform_to_stop)
	PF.stop_all(platform_to_stop)
	PF.start_all(platform_to_stop)
	PF.hc_all(platform_to_stop)