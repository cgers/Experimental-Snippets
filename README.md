# Experimental-Snippets
A collection of classes I find interesting - often from ChatGPT or an AI.

# Directed Acyclic Graphs (DAGs)

A **Directed Acyclic Graph (DAG)** is a graph structure made up of **nodes (vertices)** and **directed edges (arrows)** connecting them, with the key property that **no cycles exist** — meaning you can’t start at one node and follow the directed edges to return to the same node.

## Key Characteristics

- **Directed** → Each edge has a direction (A → B means “A leads to B”).  
- **Acyclic** → No loops or cycles.  
- **Topological order** → Nodes can be arranged linearly so that all edges go from earlier to later nodes.

## Common Uses

- **Data processing pipelines** (e.g., Airflow, Spark)  
  DAGs define dependencies between tasks — ensuring tasks run in the correct order without cycles.

- **Version control** (e.g., Git)  
  Commits form a DAG showing how versions branch and merge.

- **Build systems** (e.g., Make, Bazel)  
  Show how artifacts depend on each other to avoid redundant builds.

- **Compilers**  
  Represent expressions or operations to optimize instruction order.

- **Dependency resolution**  
  Used to model software package dependencies.

- **Blockchain / crypto**  
  Some newer blockchains (e.g., IOTA’s Tangle) use DAGs instead of linear chains.

---

In short — a DAG is a **way to represent dependencies** and **enforce order without loops**, making it ideal for workflows, computation graphs, and dependency management.
