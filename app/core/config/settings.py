from dynaconf import Dynaconf

settings = Dynaconf(
    # dynaconf 在搜索文件时用作起点的工作路径
    root_path='app/core/config',
    # 环境变量前缀，默认为 DYNACONF，如果设置为 MYPROGRAM，那么环境变量就应该以 MYPROGRAM_ 开头
    # 例如 export MYPROGRAM_FOO=bar，则就可以通过 settings.foo 获取到 bar
    envvar_prefix="DYNACONF",
    # 用于指定配置文件的名称，可以是一个列表，列表中的文件会按顺序进行加载
    settings_files=['settings.yaml', '.secrets.yaml'],
    # 如果要根据不同的环境使用不同的配置，environments 必须设置为 True，并且配置文件中必须包含多套属性
    # 例如 settings.yaml 中包含 [development] 和 [production] 两套配置
    environments=True,
)