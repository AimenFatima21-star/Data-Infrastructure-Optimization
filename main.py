"""
Main Orchestrator - Run all components
"""

from storage_benchmark import StorageBenchmark
from spark_optimization import SparkPerformanceOptimizer
from delta_transactions import DeltaTransactionManager


def run_all_benchmarks():
    """Run all benchmarks and print reports."""
    print("\n" + "="*80)
    print("        COMPLETE DATA ENGINEERING BENCHMARK SUITE")
    print("="*80)
    
    # 1. Storage Benchmark
    print("\n" + "="*80)
    print("        1. STORAGE FORMAT BENCHMARK")
    print("="*80)
    storage = StorageBenchmark()
    print(storage.generate_report())
    
    # 2. Spark Optimization
    print("\n" + "="*80)
    print("        2. SPARK PERFORMANCE OPTIMIZATION")
    print("="*80)
    spark = SparkPerformanceOptimizer()
    print(spark.generate_comparison_report())
    
    # 3. Delta Lake Transactions
    print("\n" + "="*80)
    print("        3. DATA LAKE TRANSACTION MANAGEMENT")
    print("="*80)
    delta = DeltaTransactionManager()
    delta.create_table("customer_data", [{"id": 1, "name": "Alice"}])
    delta.atomic_merge("customer_data", [{"id": 2, "name": "Bob"}], "id")
    print(delta.generate_report())
    
    print("\n" + "="*80)
    print("        ✅ ALL BENCHMARKS COMPLETE")
    print("="*80)


if __name__ == "__main__":
    run_all_benchmarks()