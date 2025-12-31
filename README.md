# 🐦 Self-Learning Flappy Bird: AI Powered by NEAT

![Python Version](https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-orange?style=for-the-badge)
![AI Framework](https://img.shields.io/badge/AI-NeuroEvolution-red?style=for-the-badge)

A cutting-edge implementation of **NEAT (NeuroEvolution of Augmenting Topologies)** algorithm that trains an AI to master Flappy Bird through evolutionary learning. Watch as a population of neural networks evolves from random flapping to superhuman performance in just a handful of generations.

---

## 🎯 Project Overview

This project demonstrates **Reinforcement Learning** combined with **Genetic Algorithms** to solve a game-playing task. Rather than hard-coding rules or using supervised learning, the AI evolves its own neural network topology and weights to achieve optimal performance.

### Key Innovation
- **Adaptive Neural Architecture:** The NEAT algorithm doesn't just optimize weights—it evolves the network structure itself, adding neurons and connections as needed
- **Population-Based Learning:** Multiple birds compete simultaneously, with the best performers "breeding" to create the next generation
- **Real-time Visualization:** Observe the learning process live as birds improve generation by generation

---

## 📚 How the AI Works

### 1. **The Environment: Flappy Bird Game**
The game engine (built with Pygame) presents a procedurally generated obstacle course:
- Vertical scrolling pipes of random heights
- Gravity-based physics applied to the bird
- Collision detection with pipes and ground
- Score incremented for successfully passing each pipe

### 2. **The Neural Network Brain**
Each bird is controlled by a lightweight feed-forward neural network:

```
Input Layer (3 neurons)
    ├─ Bird's Y Position (normalized 0-1)
    ├─ Distance to Next Pipe (pixels)
    └─ Pipe Gap Height (relative position)
         ↓
Hidden Layer(s) (Evolved dynamically)
         ↓
Output Layer (1 neuron)
    └─ Jump Decision (0 = no jump, 1 = jump)
```

### 3. **The Fitness Function: Measuring Success**
Each bird's "intelligence" is quantified by:
```
Fitness = Frames Alive + (Pipes Passed × 100)
```

This encourages both survival and progress through obstacles.

### 4. **The Evolution Process (Generation Cycle)**

```
[Generation N]
   ↓
[Play Game] → All birds play until they crash
   ↓
[Evaluate] → Calculate fitness score for each bird
   ↓
[Select] → Keep top 20% performers (elitism)
   ↓
[Breed] → Best birds' neural networks are:
   • Copied exactly (reproduction)
   • Mutated (weights ±10%)
   • Crossover combined (hybrid networks)
   ↓
[Speciation] → Group similar birds to protect innovations
   ↓
[Generation N+1] → New population plays
```

### 5. **Why NEAT Wins**
Unlike fixed-architecture algorithms (standard neural networks), NEAT automatically discovers optimal network complexity:
- **Early generations:** Simple networks (fewer neurons)
- **Needed improvement:** Automatically adds neurons and connections
- **Final solution:** Minimal but effective network architecture

---

## 🚀 Features

✅ **Real-time Evolutionary Learning**
- Watch the AI improve visually with each generation
- Live performance metrics displayed on screen

✅ **NEAT Algorithm Implementation**
- Topological mutation (add/remove nodes and connections)
- Weight mutation for fine-tuning
- Speciation to preserve diversity

✅ **Configurable Parameters**
- Population size (more = slower but better convergence)
- Mutation rates and strength
- Fitness thresholds for victory conditions

✅ **High-Performance Game Engine**
- Pygame-based rendering optimized for real-time display
- Pixel-perfect collision detection using masks
- 60+ FPS smooth gameplay

✅ **Detailed Score Tracking**
- Best fitness per generation
- Species diversity metrics
- Convergence visualization

---

## 🛠️ Installation

### Prerequisites
- **Python 3.8 or higher** (tested on Python 3.10+)
- **pip** (Python package manager)

### Step-by-Step Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/rmn2178/Self_learning_flappy_bird.git
   cd Self_learning_flappy_bird
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
   
   Or install manually:
   ```bash
   pip install pygame==2.5.2
   pip install neat-python==0.92
   ```

4. **Run the trainer:**
   ```bash
   python main.py
   ```

### What You'll See
- A Pygame window opens showing the game environment
- Multiple bird characters on screen simultaneously
- Score and generation counter at the top
- Console output showing fitness statistics

---

## ⚙️ Configuration

The `config-feedforward.txt` file controls NEAT algorithm behavior. Key parameters:

| Parameter | Default | Description |
|-----------|---------|-------------|
| `pop_size` | 50 | Number of birds per generation |
| `feed_forward` | true | Use feed-forward (vs recurrent) networks |
| `activation_default` | tanh | Neuron activation function |
| `activation_mutate_rate` | 0.0 | Probability of changing activation |
| `activation_options` | tanh | Available activation functions |
| `weight_init_mean` | 0.0 | Initial weight distribution mean |
| `weight_init_stdev` | 1.0 | Initial weight distribution std dev |
| `weight_init_type` | gaussian | How weights are initialized |
| `feed_forward` | true | Network is feed-forward (not recurrent) |
| `compatibility_threshold` | 3.0 | Distance threshold for speciation |

### Tweaking for Better Results

**Faster Convergence:**
```
pop_size = 100              # More birds = better sampling
generations = 50            # Increase training epochs
```

**Better Generalization:**
```
weight_mutation_power = 0.8
weight_replace_rate = 0.1
```

**Stability:**
```
species_elitism = 2         # Preserve top species
elitism = 5                 # Keep best 5 birds alive
```

---

## 📁 Project Structure

```
Self_learning_flappy_bird/
├── main.py                      # Main training loop and NEAT integration
├── config-feedforward.txt       # NEAT algorithm hyperparameters
├── requirements.txt             # Python dependencies
├── imgs/                        # Game assets
│   ├── bird.png                # Bird sprite (34×24px)
│   ├── pipe.png                # Pipe sprite (52×320px)
│   ├── base.png                # Ground sprite (336×112px)
│   └── background.png          # Background (288×512px)
├── winner-net                   # Best neural network (checkpoint)
├── winner-genome               # Best genome weights (checkpoint)
└── README.md                    # Documentation (this file)
```

---

## 🎮 Usage Guide

### Basic Training

Run the default trainer:
```bash
python main.py
```

The script will:
1. Load the NEAT configuration
2. Initialize a population of 50 random birds
3. Begin the evolutionary process
4. Display live game visualization
5. Print generation statistics to console

### Console Output Example
```
Generation 1 | Best: 145.2 | Avg: 52.3 | Species: 3
Generation 2 | Best: 312.1 | Avg: 118.5 | Species: 4
Generation 3 | Best: 587.9 | Avg: 289.2 | Species: 3
...
Generation 10 | Best: 9999.0 | Avg: 8521.3 | Species: 2
```

### Performance Targets
| Metric | Timeframe | Expected |
|--------|-----------|----------|
| First win (survival) | Gen 1-3 | Bird passes first pipe |
| Consistent passing | Gen 5-8 | Bird passes 5+ pipes |
| Near-perfect play | Gen 10-15 | Bird plays indefinitely |

---

## 🔬 Technical Deep Dive

### Neural Network Representation

Each bird's decision-making is encoded as a **directed acyclic graph (DAG)**:

```
Inputs: [y_pos, pipe_dist, pipe_gap]
              ↓
       [Hidden Neurons]  ← Topology evolves here
              ↓
       [Output Neuron] → Jump: Yes/No
```

### Mutation Operations

**1. Add Node Mutation**
```
Before: Input → Output (1 connection)
After:  Input → Hidden → Output (2 connections)
        The old weight is split: new weights sum to original
```

**2. Add Connection Mutation**
```
Before: Input1 ──→ Output
        Input2 ──⊗ (no connection)
After:  Input1 ──→ Output
        Input2 ──→ (new connection added)
```

**3. Weight Mutation**
```
w_new = w_old + N(0, σ²)  where σ controlled by config
```

### Speciation Algorithm

Birds are grouped by genetic distance:
```
Distance = c1 × (excess genes) + c2 × (disjoint genes) + c3 × (weight diff)
```

If distance < threshold: Birds in same species
If distance ≥ threshold: Birds in different species

**Benefit:** Different species can explore different solutions without being outcompeted too quickly.

---

## 🎓 Learning Outcomes

Building this project teaches:

✅ **Evolutionary Algorithms**
- Population-based optimization
- Natural selection and genetic operators
- Speciation and niching strategies

✅ **Neural Networks**
- Network topology design
- Activation functions
- Forward propagation

✅ **Game Development**
- Pygame library fundamentals
- Collision detection
- Real-time rendering

✅ **Python Advanced Topics**
- Object-oriented design
- Configuration file parsing
- Graph data structures

---

## 📊 Results & Benchmarks

### Expected Performance Over Time

```
Generation  | Best Score | Avg Score | Key Milestone
────────────┼────────────┼───────────┼──────────────────
1           | 89         | 34        | First pipe passed
3           | 412        | 156       | Consistent play
5           | 1,250      | 540       | Multiple pipes
8           | 4,800      | 2,100     | Expert-level play
12          | 10,000+    | 8,000+    | Near-optimal
```

### Hardware Requirements
- **CPU:** Any modern processor (no GPU required)
- **RAM:** 512 MB minimum, 2 GB recommended
- **Disk:** 100 MB
- **Runtime:** 2-10 minutes per full training on CPU

---

## 🔧 Troubleshooting

### Issue: "No module named 'pygame'"
**Solution:**
```bash
pip install pygame --upgrade
```

### Issue: "ModuleNotFoundError: No module named 'neat'"
**Solution:**
```bash
pip install neat-python
```

### Issue: Window doesn't display or crashes
**Solution:**
- Ensure you have a display (headless systems won't work without modification)
- Try updating Pygame: `pip install --upgrade pygame`
- Check that your graphics drivers are up-to-date

### Issue: Training is very slow
**Solution:**
- Reduce `pop_size` in config (from 50 to 25)
- Disable visualization temporarily (add headless mode)
- Use a faster CPU/GPU if available

---

## 🚀 Enhancement Ideas

### Beginner-Level
- [ ] Save the best bird's network and replay it without training
- [ ] Add adjustable game difficulty (pipe spacing, speed)
- [ ] Create a statistics graph showing fitness over generations

### Intermediate-Level
- [ ] Implement recurrent neural networks (LSTM cells)
- [ ] Add different input sensory options (bird angle, velocity)
- [ ] Create a human vs AI mode to compete with the trained bird

### Advanced-Level
- [ ] Parallelize evolution across multiple processes
- [ ] Implement multi-objective optimization (fitness + network complexity)
- [ ] Export trained network to ONNX format for deployment
- [ ] Add advanced visualization: Show activated neurons lighting up in real-time

---

## 📚 Resources & References

### NEAT Algorithm
- **Original Paper:** *Evolving Neural Networks Through Augmenting Topologies* (Stanley & Miikkulainen, 2002)
- **NEAT-Python Docs:** https://neat-python.readthedocs.io/
- **Algorithm Visualization:** https://neat.wikidot.com/

### Game Development
- **Pygame Tutorial:** https://www.pygame.org/docs/
- **Flappy Bird Mechanics:** https://github.com/topics/flappy-bird

### Machine Learning Theory
- **Evolutionary Algorithms:** https://en.wikipedia.org/wiki/Evolutionary_algorithm
- **Reinforcement Learning:** https://www.deepmind.com/publications

---

## 🤝 Contributing

Contributions are welcome! Please follow these guidelines:

1. **Fork the repository** on GitHub
2. **Create a feature branch:**
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Make your changes** with clear, descriptive commits
4. **Test thoroughly** to ensure nothing breaks
5. **Submit a pull request** with a detailed description

### Areas for Contribution
- Improved fitness functions
- Alternative game mechanics
- Performance optimizations
- Documentation enhancements
- Visualization improvements

---

## 📝 License

This project is licensed under the **MIT License** - see the LICENSE file for details.

You are free to:
- ✅ Use this in commercial projects
- ✅ Modify and distribute
- ✅ Use privately

You must:
- ✅ Include the original copyright notice
- ✅ Include the license text

---

## 👨‍💻 Author

**GitHub:** [@rmn2178](https://github.com/rmn2178)

This project was developed as part of my journey into Machine Learning and AI, demonstrating practical applications of evolutionary algorithms and neural networks.

---

## ⭐ Acknowledgments

- **NEAT Algorithm:** Kenneth O. Stanley and Risto Miikkulainen
- **NEAT-Python Library:** Contributors and maintainers
- **Pygame Community:** For excellent game development tools
- **Flappy Bird:** Original game by Dong Nguyen

---

## 📞 Support & Questions

- **Issues:** Report bugs on [GitHub Issues](https://github.com/rmn2178/Self_learning_flappy_bird/issues)
- **Discussions:** Start a [GitHub Discussion](https://github.com/rmn2178/Self_learning_flappy_bird/discussions)
- **Email:** [Your Contact Info]

---

> 🎯 **Pro Tip:** Star this repository if you find it helpful! It motivates continued development and helps others discover the project.

**Made with ❤️ for AI enthusiasts and game lovers**
