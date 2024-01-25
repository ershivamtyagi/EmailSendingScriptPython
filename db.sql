-- Table to store email configurations
CREATE TABLE email_config (
    id INT AUTO_INCREMENT PRIMARY KEY,
    smtp_host VARCHAR(255) NOT NULL,
    smtp_port INT NOT NULL,
    smtp_user VARCHAR(255) NOT NULL,
    smtp_password VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table to store MySQL configurations
CREATE TABLE mysql_config (
    id INT AUTO_INCREMENT PRIMARY KEY,
    mysql_host VARCHAR(255) NOT NULL,
    mysql_user VARCHAR(255) NOT NULL,
    mysql_password VARCHAR(255) NOT NULL,
    mysql_database VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table to store users
CREATE TABLE user (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL,
    creation_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    preferred_language VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table to store daily questions
CREATE TABLE daily_questions (
    day_id INT PRIMARY KEY,
    question VARCHAR(255) NOT NULL,
    description VARCHAR(255),
    intuition VARCHAR(255),
    brute_force VARCHAR(255),
    complexitybf VARCHAR(255),
    better1 VARCHAR(255),
    complexity_b VARCHAR(255),
    optimal VARCHAR(255),
    complexity_o VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table to store email logs
CREATE TABLE email_log (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    email_to VARCHAR(255) NOT NULL,
    status VARCHAR(50) NOT NULL,
    log_message TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES user(id)
);
