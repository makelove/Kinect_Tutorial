##

- 摘要
    - The long-term goal of our work is to get away from precise, but very expensive robotic systems and to develop affordable, potentially imprecise
        - > 我们工作的长期目标是，放弃那些精准但非常昂贵的机器人系统，去发展不是很精准但一般人支付得起的
    - self-adaptive manipulator systems that can interactively perform tasks such as playing with children
        - > 自主适应的操作器系统，可以互动地执行任务，例如，和小孩子玩耍
     - demonstrate how a low-cost off-the-shelf robotic system can learn closed-loop policies for a stacking task in only a handful of trials—from scratch. 
        - >演示如何只在 一些 从草稿开始, 低成本的现成的机器人系统,能学习 闭环策略 堆积木任务 
     - no pose feedback 没有 姿势反馈  
     - Kinect-style depth camera 深度相机
     - model-based reinforcement learning technique. 基于模型的强化学习技术
     - Our learning method is data efficient, reduces model bias, and deals with several noise sources in a principled way during long-term planning.
        - >我们的学习方法是数据效应,减少模型误差,在长期规划中用有原则的途经,处理几种噪音来源
     - We present a way of incorporating state-space constraints into the learning process and analyze the learning gain by exploiting the sequential structure of the stacking task.
        - >我们展示一种将,状态空间约束,与学习过程相结合的方法，并利用堆积木任务的,顺序结构来分析,学习增益。
- I. INTRODUCTION介绍
    -  While ex-isting techniques have the potential to solve various household manipulation tasks, they typically rely on extremely expensive robot hardware
        - > 现有的技术有潜力去解决各种的日常操作任务,但他们很大程度上依赖非常昂贵的机器人硬件
        