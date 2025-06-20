import numpy as np

def main():
    """Inventory Management System với NumPy"""
    print("=== INVENTORY MANAGEMENT SYSTEM ===")
    print()
    
    # Tạo inventory database
    np.random.seed(42)
    n_products = 50
    
    product_ids = np.arange(1001, 1001 + n_products)
    quantities = np.random.randint(0, 100, n_products)
    prices = np.random.uniform(10, 500, n_products)
    costs = prices * np.random.uniform(0.5, 0.8, n_products)
    weekly_sales = np.random.randint(1, 15, n_products)
    
    # Inventory overview
    total_stock = np.sum(quantities)
    total_value = np.sum(quantities * prices)
    avg_price = np.mean(prices)
    
    print("📦 INVENTORY OVERVIEW:")
    print(f"Total products: {n_products}")
    print(f"Total stock units: {total_stock:,}")
    print(f"Total inventory value: ${total_value:,.2f}")
    print(f"Average price per item: ${avg_price:.2f}")
    print()
    
    # Sorting - Top 5 most expensive
    print("🔍 SORTING & SEARCHING:")
    print()
    expensive_indices = np.argsort(prices)[::-1][:5]  # Top 5
    
    print("Top 5 Most Expensive Products:")
    for idx in expensive_indices:
        product_value = quantities[idx] * prices[idx]
        print(f"ID: {product_ids[idx]} | Price: ${prices[idx]:.2f} | "
              f"Stock: {quantities[idx]} | Value: ${product_value:,.2f}")
    print()
    
    # Low stock alert
    print("⚠️  LOW STOCK ALERT (< 10 units):")
    low_stock_mask = quantities < 10
    low_stock_indices = np.where(low_stock_mask)[0]
    
    for idx in low_stock_indices:
        status = "CRITICAL" if quantities[idx] < 5 else "LOW"
        print(f"ID: {product_ids[idx]} | Stock: {quantities[idx]} | "
              f"Price: ${prices[idx]:.2f} | Status: {status}")
    print()
    
    # Revenue analysis
    print("📊 REVENUE ANALYSIS:")
    expensive_products = np.sum(prices > 300)
    expensive_percentage = expensive_products / n_products * 100
    
    high_value_items = np.sum((quantities * prices) > 10000)
    potential_revenue = np.sum(quantities * prices)
    profit_margin = np.mean((prices - costs) / prices) * 100
    
    print(f"Products > $300: {expensive_products} items ({expensive_percentage:.1f}%)")
    print(f"High-value stock (>$10k): {high_value_items} items")
    print(f"Potential revenue: ${potential_revenue:,.2f}")
    print(f"Estimated profit margin: {profit_margin:.1f}%")
    print()
    
    # Reorder suggestions
    print("📋 REORDER SUGGESTIONS:")
    
    # Priority based on stock level vs weekly sales
    days_of_stock = quantities / (weekly_sales + 0.1)  # Avoid division by zero
    critical_items = np.where((quantities < 10) & (days_of_stock < 7))[0]
    
    # Sort by urgency (lowest days of stock first)
    priority_order = np.argsort(days_of_stock[critical_items])
    
    for i, idx in enumerate(critical_items[priority_order][:3], 1):
        print(f"Priority {i}: Product {product_ids[idx]} "
              f"(Stock: {quantities[idx]}, Weekly sales: {weekly_sales[idx]})")
    print()
    
    print("Suggested reorder quantities:")
    for idx in critical_items[priority_order][:3]:
        # Suggest 4 weeks of stock
        suggested_qty = weekly_sales[idx] * 4
        reorder_cost = suggested_qty * costs[idx]
        print(f"ID {product_ids[idx]}: Order {suggested_qty} units "
              f"(Cost: ${reorder_cost:,.2f})")
    print()
    
    # Additional analytics
    print("📈 ADDITIONAL ANALYTICS:")
    print(f"Fastest moving item: ID {product_ids[np.argmax(weekly_sales)]} "
          f"({np.max(weekly_sales)} units/week)")
    print(f"Slowest moving item: ID {product_ids[np.argmin(weekly_sales)]} "
          f"({np.min(weekly_sales)} units/week)")
    print(f"Most profitable item: ID {product_ids[np.argmax(prices - costs)]} "
          f"(${np.max(prices - costs):.2f} profit/unit)")

if __name__ == "__main__":
    main()
