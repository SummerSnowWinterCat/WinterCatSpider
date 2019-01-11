import configparser


# 配置文件读取
def read_config(config_name, get_entity):
    config = configparser.ConfigParser()
    config.read('mysql_config.ini', encoding='utf-8')
    return config.get(config_name, get_entity)


# 添加
def set_config(config_name, option_name, get_entity, ):
    config = configparser.ConfigParser()
    config.read('mysql_config.ini', encoding='utf-8')
    config.set(config_name, option_name, get_entity)
    config.write(open('mysql_config.ini', 'w', encoding='utf-8'))
    print('<config save success>')
    return 1

