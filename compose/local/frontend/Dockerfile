# Base image
FROM node:20-alpine AS base

ENV NODE_VERSION 20.14.0

# 1. Install dependencies only when needed
FROM base AS deps
# Check https://github.com/nodejs/docker-node/tree/b4117f9333da4138b03a546ec926ef50a31506c3#nodealpine to understand why libc6-compat might be needed.
RUN apk add --no-cache libc6-compat

WORKDIR /app

# Install dependencies based on the preferred package manager
COPY ../frontend/package.json ../frontend/package-lock.json ./
RUN npm install --frozen-lockfile

# 2. Local development setup
FROM base AS dev
WORKDIR /app

ENV NODE_ENV=development

# Copy dependencies from deps stage
COPY --from=deps /app/node_modules ./node_modules

# Copy the entire frontend folder for local development
COPY ../frontend ./

USER node

EXPOSE 3000

# Command to run the Next.js app in development mode
CMD ["npm", "run", "dev"]
