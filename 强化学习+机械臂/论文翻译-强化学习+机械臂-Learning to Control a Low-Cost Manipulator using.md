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
    - how to use a cheap, off-the-shelf robotic manipulator ($370) and a Kinect- style (http://www.xbox.com/kinect) depth camera (<$120) to learn a block stacking task under state-space constraints.
        - > 如何使用 便宜的 现成的 机械臂 370美元,和 Kinect风格深度相机 小于120美元,在状态空间约束下,去学习堆积木任务
    - Fully autonomous RL methods typically require many trials to successfully solve a task
        - > 全自动 强化学习 方法,主要 需要 很多次尝试,才能成功解决一个任务
    - If this knowledge is unavailable, due to the lack of understanding of complicated dynamics or because a solution is simply not known, data-intensive learning methods are required. 
        - > 如果,知识不可用,由于缺少对复杂 动力学 的理解,或者因为 一个方案是不可知,那么数据密集型学习方法就是必需的
    - To sidestep these problems, we build on PILCO (probabilistic inference for learning control), a data-efficient model-based (indirect) policy search method 搜索策略 that reduces减少 model bias误差 ,a typical 典型problem of model-based methods: PILCO employs使用 a flexible 灵活 probabilistic概率性的 non-parametric非参数化  Gaussian高斯 process (GP) dynamics model动态模型 and takes model uncertainty模型不确定性 consistently一致地 into account during long-term planning长期规划. 
       - 为躲过这些问题,我们打造一个基于PILCO
    - how obstacle障碍 information provided提供 by the depth camera can be incorporated合并 into PILCO’s planning and learning to avoid collisions避开碰撞 even during training, and how knowledge知识 can be efficiently 有效地transferred转化 across related相关 tasks
    
- II. RELATED WORK  相关工作  
    - Motor babbling is data-inefficient and does not guarantee good models along a good trajectory
        - >电机含糊不清,摆动,是 数据低效率,不能在好的运动轨迹中,保证好的模型
    - Reducing model bias requires accounting for model uncertainty during planning
        - > 减少模型误差,需要 在规划过程中 模型不确定性 的统计工作
        
- III. PRELIMINARIES 初步工作   
     - 4个假设
     - 机械臂Lynxmotion http://www.lynxmotion.com/c-27-robotic-arms.aspx
        - 6自由度 
            - 1 base rotate, 234 three joints,5 wrist rotate, and a gripper (open/close)6.
     - Instead of equipping the robot with further sensors and/or markers, we demonstrate that good controllers can be learned without additional information.
        - > 我们演示,好的控制器可以在没有额外信息的情况下去学习怎样运动,而不是用很多传感器和标记去装备它    
     - PrimeSense depth camera深度相机
        - 640 × 480 color RGB, 30Hz.
        - 深度 距离0.5 m–5 m
            - 分辨率 在距离2米时是1 cm
     - ROS handles the communication with the hardware.
            - ROS机器人操作系统 负责与硬件通信
     - B. Block Tracking
        - Assuming that the object has a uniform color, we use color-based region growing starting at the clicked pixel to estimate the extent and 3D center of the object,
            - >假设 物体有相同的颜色,我们使用居于颜色区域 周围在点击的像素去建立 物体的周长和3D中心
- IV. POLICY LEARNING WITH STATE-SPACE CONSTRAINTS
     - 
     
- In a classical RL setup, it is assumed that the learner is not aware of any constraints in the state space, but has to discover walls etc. by running into them and gaining a high penalty.
     - >在经典的RL配置,它假设学习者在状态空间内不能感知任何约束,但不得不去发现墙壁,通过如果撞到墙会受到高的惩罚
     