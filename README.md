### Future Research Areas in RL

## General value functions and Auxiliary methods
- TWe should be able to generalize beyond rewards to permit predictions about arbitrary signals. Rather than predicting the sum of future rewards, we might predict the sum of the future values of a sound or color sensation, or of an internal, highly processed signal such as another prediction. Whatever signal is added up in this way in a value-function-like prediction, we call it the cumulant of that prediction. We formalize it in a cumulant signal Ct 2 R. Using this, a general value function, or GVF, is written.
- Because a GVF has no necessary connection to reward, it is perhaps a misnomer to call it a value function. One could simply call it a prediction or, to make it more distinctive, a forecast.
- The ability to predict and control a diverse multitude of
signals can constitute a powerful kind of environmental model.making use of Auxiliary tasks for this is important .
- Eg. We might imagine an artificial neural network (ANN) in which the last layer is split into multiple parts, or heads, each working on a di↵erent task. One head might produce the approximate value function for the main task (with reward as its cumulant) whereas the others would produce solutions to various auxiliary tasks.
- Researchers have experimented with auxiliary tasks such as predicting change in pixels, predicting the next time step’s reward, and predicting the distribution of the return. In many cases this approach has been shown to greatly accelerate learning on the main task (Jaderberg et al., 2017).

## Temporal Abstractions via options
- One can use it to formalize the task of deciding which muscles to twitch to grasp an object, which airplane flight to take to arrive conveniently at a distant city, and which job to take to lead a satisfying life. These tasks differ greatly in their time scales, yet each can be usefully formulated as an MDP
- Although all these tasks can be formulated as MDPs, one might think that they cannot be formulated as a single MDP. They involve such di↵erent time scales, such different notions of choice and action!
- The Question to answer is can the MDP framework be used to cover all levels of diverse problems ? say , the muscle twiches level cannot be extended to plan a flight across a continent. But , tasks like throwing , grabbing and hitting a baseball can be.
- It can and one popular idea is to formalize an MDP at a detailed level, with a small time step, yet enable planning at higher levels using extended courses of action that correspond to many base-level time steps
- We need to understand the notion of course of action and notion of termination. A general way to formulate this is with the policy "pi" and a state dependent termination function "gamma". We define a pair of these as a generalized ntoion of action called **Options**.
- To execute an option ``` omega = <pi,gamma>``` at time t is to obtain the action to take , A(t) from ```pi(·|St)```, then terminate at time t + 1 with probability ```1 − gamma(St+1)```. If the option does not terminate at t+1, then At+1 is selected from ```pi(·|St+1)```, and the option terminates at
t+2 with probability ```1−gamma(St+2)```, and so on until eventual termination.

- Each action ```a``` corresponds to an option ```omega = <pi, gamma>```
- The notion of an action-value function ```q(pi)``` naturally generalizes to an optionvalue function that takes a state and option as input and returns the expected return starting from that state, executing that option to termination, and thereafter following the policy, "pi". We can also generalize the notion of policy to a hierarchical policy that selects from options rather than actions, where options, when selected, execute until termination.
- So , we can instead learn approximate option-value functions and hierarchical policies.

## Designing better Reward Signals
- By designing a reward signal we mean designing the part of an agent’s environment that is responsible for computing each scalar reward Rt and sending it to the agent at each time t.
- This is easy to built for specific tasks where the goal to be achieved is straigtforward. But some problems involve goals that are difficult to translate into reward signals. This is especially true when the problem requires the agent to skillfully perform a complex task or set of tasks, such as would be required of a useful household robotic assistant.
- In cases of simple and easily identifiable goals also the problem of  *sparse rewards* arises.
- A particularly e↵ective approach to the sparse reward problem is the **shaping** technique introduced by the psychologist B. F. Skinner.
- Shaping involves changing the reward signal as learning proceeds, starting from a reward signal that is not sparse given the agent’s initial behavior, and gradually modifying it toward the reward signal suited to problem of original interest. Shaping might also involve modifying the dynamics of the task as learning proceeds. Each modification is made so that the
agent is frequently rewarded given its current behavior. The agent faces a sequence of increasingly-difficult reinforcement learning problems, where what is learned at each stage makes the next-harder problem relatively easy because the agent now encounters reward more frequently than it would if it did not have prior experience with easier problems.This kind of shaping is an essential technique in training animals, and it is e↵ective in
computational reinforcement learning as well.
- Reward mechanisms can be learned by "imitation learning ", "apprenticeship learning", where the machine learns watching a person who is already an expert at the task.
- Learning from an expert’s behavior can be done either by learning directly by supervised learning or by extracting a reward signal using what is known as “inverse reinforcement learning” and then using a reinforcement learning algorithm with that reward signal to learn a policy.
- Another approach to finding a good reward signal is to automate the trial-and-error search for a good signal.
- From an application perspective, the reward signal is a parameter of the learning algorithm. As is true for other algorithm parameters, the search for a good reward signal can be automated by defining a space of feasible candidates and applying an optimization algorithm.
- The optimization algorithm evaluates each candidate reward signal by running the reinforcement learning system with that signal for some number of steps, and then scoring the overall result by a “high-level” objective function intended to encode the designer’s true goal, ignoring the limitations
of the agent.

## Issues to be addressed/Future Scope
1. We still need powerful parametric function approximation techniques that work well in fully increamental and online settings.
   - Methods based on deep learning and ANNs area major step in this direction but, still, only work well with batch training on large data sets, with training from extensive offline self play, or with learning from the interleaved experience of multiple agents on the same task.
   - These and other settings are ways of working around a basic limitation of today’s deep learning methods, which struggle to learn rapidly in the incremental, online settings that are most natural for the reinforcement learning algorithms emphasized. The problem is sometimes described as one of “catastrophic interference” or “correlated data.”
   - When something new is learned it tends to replace what has previously been learned rather than adding to it, with the result that the benefit of the older learning is lost. Techniques such as “replay buffers” are often used to retain and replay old data so that its benefits are not permanently lost.

2. We still need methods for learning features such that subsequent learning generalizes well.
   - This issue is an instance of a general problem variously called “representation learning,” “constructive induction,” and “meta-learning”— how can we use experience not just to learn a given desired function, but to learn inductive biases such that future learning generalizes better and is thus faster?
   - It is also less common to explore representation learning within a reinforcement learning context. (See works in ICLR)
   - With use of Auxiliary tasks reinforcement learning can bring new possibilties
   -  In reinforcement learning, the problem of representation learning can be identified with the problem of learning the state-update function.(Using POMDPs)

3. We still need scalable methods for planning with learned environment models
    - Exploring this with temporally-abstract models using options framework
    - Exploring linear models
    - Cases of full model-based reinforcement learning, in which the environment model is learned from data and then used for planning, are rare.   

4. Future scope also revolves around automating the choice of tasks on which an agent works and uses to structure its developing competence.
    - It is usual in machine learning for human designers to set the tasks that the learning agent is expected to master. Because these tasks are known in advance and remain fixed, they can be built into the learning algorithm code.
    - we will want the agent to make its own choices about what tasks it should try to master. These might be subtasks of a specific overall task that is already known, or they might be intended to create building blocks that permit more efficient learning of many different tasks that the agent is likely to face in the future but which are currently unknown.

5. The fifth issue that we would like to highlight for future research is that of the interaction between behavior and learning via some computational analog of curiosity. (Concept of Intrinsic reward signals)
    - When reward is not available, or notstrongly influenced by behavior, the agent is free to choose actions that maximize in some sense the learning on the tasks, that is, to use some measure of learning progress     as an internal or “intrinsic” reward, implementing a computational form of curiosity.
    - In addition to measuring learning progress, intrinsic reward can, among other possibilities, signal the receipt of  unexpected, novel, or otherwise interesting input, or can assess the agent’s ability to cause changes in its environment.   
    - Intrinsic reward signals generated in these ways can be used by an agent to pose tasks for itself by defining auxiliary tasks, GVFs, or options, as discussed above, so that skills learned in this way can contribute to the agent’s ability to master future tasks.
6. Developing methods to make it acceptably safe to embed reinforcement learning agents into physical environments.
