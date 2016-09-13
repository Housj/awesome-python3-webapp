configs = configs_default.configs

try:
	import config_override
	configs = merge(configs,config_override.configs)
except ImportError:
	pass