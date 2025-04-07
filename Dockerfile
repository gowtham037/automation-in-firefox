# Start with an official Python base image
FROM python:3.11-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    curl \
    wget \
    unzip \
    nano \
    openjdk-17-jdk \
    git \
    xvfb \
    gnupg2 \
    libgtk-3-0 \
    libnss3 \
    libgconf-2-4 \
    libasound2 \
    libxss1 \
    libxi6 \
    libdbus-glib-1-2 \
    firefox-esr \
    && rm -rf /var/lib/apt/lists/*

# Set environment variables
ENV JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
ENV PATH=$JAVA_HOME/bin:$PATH

# Install Geckodriver
RUN GECKO_VERSION=$(curl -s https://api.github.com/repos/mozilla/geckodriver/releases/latest | grep 'tag_name' | cut -d '"' -f 4) && \
    wget https://github.com/mozilla/geckodriver/releases/download/$GECKO_VERSION/geckodriver-$GECKO_VERSION-linux64.tar.gz && \
    tar -xzf geckodriver-$GECKO_VERSION-linux64.tar.gz && \
    mv geckodriver /usr/local/bin/ && \
    chmod +x /usr/local/bin/geckodriver && \
    geckodriver --version

# Install Node.js and Appium
RUN curl -fsSL https://deb.nodesource.com/setup_18.x | bash - && \
    apt-get update && \
    apt-get install -y nodejs && \
    npm install -g appium

# Install Appium drivers
RUN appium driver install gecko

# Install Appium Doctor (optional but useful)
RUN npm install -g appium-doctor

# Install Python packages
RUN pip install --upgrade pip && \
    pip install selenium appium-python-client

# Add a non-root user
RUN useradd -ms /bin/bash appiumuser
USER appiumuser
WORKDIR /home/appiumuser

# Expose Appium port
EXPOSE 4723

# Default command
CMD ["appium"]

