-- Mutual Fund Analytics Database Schema

DROP TABLE IF EXISTS nav_history;
DROP TABLE IF EXISTS fund_master;
DROP TABLE IF EXISTS benchmark_indices;

-- Fund Master Dimension Table
CREATE TABLE fund_master (
    fund_id VARCHAR(50) PRIMARY KEY,
    fund_name VARCHAR(255) NOT NULL,
    amc_name VARCHAR(255) NOT NULL,
    category VARCHAR(100) NOT NULL,
    sub_category VARCHAR(100),
    plan_type VARCHAR(50), -- Direct or Regular
    inception_date DATE,
    expense_ratio DECIMAL(5, 2)
);

-- Daily NAV Fact Table
CREATE TABLE nav_history (
    nav_id INTEGER PRIMARY KEY AUTOINCREMENT,
    fund_id VARCHAR(50) NOT NULL,
    nav_date DATE NOT NULL,
    nav_value DECIMAL(10, 4) NOT NULL,
    daily_return DECIMAL(8, 4),
    aum_crores DECIMAL(12, 2),
    FOREIGN KEY (fund_id) REFERENCES fund_master(fund_id),
    UNIQUE(fund_id, nav_date)
);

-- Benchmark Indices Table
CREATE TABLE benchmark_indices (
    index_id VARCHAR(50) NOT NULL,
    index_name VARCHAR(255) NOT NULL,
    trade_date DATE NOT NULL,
    closing_price DECIMAL(10, 4) NOT NULL,
    daily_return DECIMAL(8, 4),
    PRIMARY KEY (index_id, trade_date)
);

-- Indexes for Query Performance
CREATE INDEX idx_nav_fund_date ON nav_history(fund_id, nav_date);
CREATE INDEX idx_benchmark_date ON benchmark_indices(index_id, trade_date);