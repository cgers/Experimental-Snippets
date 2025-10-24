namespace ClassLibrary
{
    /// <summary>
    /// Represents a directed acyclic graph (DAG) where nodes are of a specified type.
    /// </summary>
    /// <remarks>A directed acyclic graph (DAG) is a graph that is directed and contains no cycles.  This
    /// class provides functionality to add nodes, add edges, and perform a topological sort.</remarks>
    /// <typeparam name="T">The type of the nodes in the graph. The type must be non-nullable.</typeparam>
    public class DirectedAcyclicGraph<T> where T : notnull
    {
        private readonly Dictionary<T, List<T>> _adjacencyList = new();

        public void AddNode(T node)
        {
            if (!_adjacencyList.ContainsKey(node))
                _adjacencyList[node] = new List<T>();
        }

        public void AddEdge(T from, T to)
        {
            // Ensure both nodes exist before connecting them
            AddNode(from);
            AddNode(to);

            if (WouldCreateCycle(from, to))
                throw new InvalidOperationException($"Adding edge {from} → {to} would create a cycle.");

            _adjacencyList[from].Add(to);
        }

        private bool WouldCreateCycle(T start, T target)
        {
            var visited = new HashSet<T>();
            var stack = new Stack<T>();
            stack.Push(target);

            while (stack.Count > 0)
            {
                var current = stack.Pop();
                if (current.Equals(start)) return true;

                if (_adjacencyList.TryGetValue(current, out var children))
                {
                    foreach (var child in children)
                    {
                        if (visited.Add(child))
                            stack.Push(child);
                    }
                }
            }
            return false;
        }

        public List<T> TopologicalSort()
        {
            var visited = new HashSet<T>();
            var result = new Stack<T>();

            foreach (var node in _adjacencyList.Keys)
                Visit(node, visited, result);

            return result.Reverse().ToList();
        }

        private void Visit(T node, HashSet<T> visited, Stack<T> result)
        {
            if (!visited.Add(node))
                return;

            foreach (var neighbor in _adjacencyList[node])
                Visit(neighbor, visited, result);

            result.Push(node);
        }
    }

}
