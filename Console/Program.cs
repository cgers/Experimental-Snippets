using ClassLibrary;

namespace ConsoleApp
{
    internal class Program
    {
        static void Main(string[] args)
        {
            var dag = new DirectedAcyclicGraph<string>();

            // Add nodes and edges
            dag.AddEdge("Clean Data", "Train Model");
            dag.AddEdge("Load Data", "Clean Data");
            dag.AddEdge("Train Model", "Evaluate Model");
            dag.AddEdge("Evaluate Model", "Deploy Model");

            // Show topological sort (execution order)
            var order = dag.TopologicalSort();
            Console.WriteLine("Topological Sort (Execution Order):");
            Console.WriteLine(string.Join(" → ", order));

            // Try to add a cycle (should throw)
            try
            {
                dag.AddEdge("Deploy Model", "Load Data");
            }
            catch (InvalidOperationException ex)
            {
                Console.WriteLine($"\nCycle detection works: {ex.Message}");
            }
            Console.ReadKey();
        }
    }
}
