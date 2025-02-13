# Use official Node.js image
FROM node:18

# Set the working directory
WORKDIR /app

# Copy package.json and install dependencies
COPY package.json ./
RUN npm install

# Copy the rest of the frontend files
COPY . .

# Expose port 3000 for React app
EXPOSE 3000

# Start the React app
CMD ["npm", "start"]
