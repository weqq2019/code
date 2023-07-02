# [conda进行python环境隔离](https://www.cnblogs.com/moodlxs/p/11509692.html)

## 1、环境隔离的问题

在使用python时，常常遇到的问题：

pip安装库A，依赖库B-2.1版本

pip安装库C，以来库B-3.1版本，安装会提示库B的版本冲突错误。

 

这种情况下就需要做环境隔离

conda自带环境隔离功能，可以有限隔离管理多个python环境

 

## 2、安装conda

从https://www.anaconda.com/distribution/下载anaconda， 我这里下载的是Anaconda3-2019.07-Linux-x86_64.sh

转到下载目录下， 执行命令安装anaconda：

```
bash Anaconda3-2019.07-Linux-x86_64.sh
```

根据提示安装，特别是最后的conda init询问，直接点yes

 

## 3、备份conda原始环境

conda安装完成后，重新打开shell，或者执行一次source ~/.bashrc后， 会默认进入base环境，base环境包括了anaconda默认安装的大量库。

由于后续可能会基于base环境安装各种附加库，所以，一般先进行base环境的备份，方式就是创建一个新的backup环境，直接从base环境中克隆

创建backup环境的命令如下：

```
conda create -n backup --clone base
```

上述指令表示从base环境中clone一份新环境，新环境名字为backup

`conda create -n backup --clone base` 是一个 `conda` 命令，用于创建一个名为 `backup` 的新环境，并将其克隆为当前活动环境的副本。

具体而言，这个命令的含义如下：

- `conda create`：这是 `conda` 的创建环境命令。
- `-n backup`：`-n` 标志指定了新环境的名称，这里是 `backup`。
- `--clone base`：`--clone` 标志后面指定了要克隆的环境名称，这里是 `base`。`base` 是 Conda 的默认环境，也是你系统中已安装的默认环境。

因此，`conda create -n backup --clone base` 命令会在你的 Conda 环境中创建一个名为 `backup` 的新环境，并将 `base` 环境的所有包和配置克隆到这个新环境中。这样，你就可以在 `backup` 环境中进行独立的开发和测试，而不会影响或受到系统的默认环境的影响。 

## 4、创建项目环境

备份之后，就可以基于backup环境，克隆各种项目环境了

比如，我需要创建一个用于富途量化开发的环境：

```conda create -n futu --clone backup 是一个 conda 命令，用于创建一个名为 futu 的新环境，并将其克隆为已存在的 backup 环境的副本。
conda create -n futu --clone backup
```

`conda create -n futu --clone backup` 是一个 `conda` 命令，用于创建一个名为 `futu` 的新环境，并将其克隆为已存在的 `backup` 环境的副本。

具体而言，这个命令的含义如下：

- `conda create`：这是 `conda` 的创建环境命令。
- `-n futu`：`-n` 标志指定了新环境的名称，这里是 `futu`。
- `--clone backup`：`--clone` 标志后面指定了要克隆的环境名称，这里是 `backup`。

因此，`conda create -n futu --clone backup` 命令会在你的 Conda 环境中创建一个名为 `futu` 的新环境，并将已存在的 `backup` 环境的所有包和配置克隆到这个新环境中。这样，你就可以在 `futu` 环境中使用和测试与 `backup` 环境相同的软件包和设置。在该环境下，我需要安装futu-api:

```
pip insall futu-api
```

那么futu-api库只有在该环境中才有，在base、backup中都不存在。

 

如果觉得base环境过于臃肿，可以创建一个新的简洁环境， conda可以管理多个python，即使python的版本不一样，这个是比venv强大的地方。

创建一个python3.7的简洁环境：

```
conda create -n py32 python=3.7
```

 

创建一个python2.7的简洁环境：

```
conda create -n py27 python=2.7
```

 

注意：创建环境时，如果只是指定了名字，没有指定package，那么实际上指向的都是同一个环境

如：

```
conda create -n test1
conda create -n test2
```

上述的test1和test2环境中，隔离的只是conda install的内容，而pip安装的内容完全共享，会相互干扰，这是因为使用了同一套python环境的缘故， 所以一般不要这么做。

 

## 5、环境切换

通过conda activate <envname>进行环境切换

通过conda deactivate退出环境

 

如，进入futu环境：

```
conda activate  futu
```

进入环境后，命令行中会提示相应的环境标志：

![img](https://img2018.cnblogs.com/blog/361206/201909/361206-20190912003843828-1357513492.png)