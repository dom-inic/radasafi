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

# 2. Rebuild the source code only when needed
FROM base AS builder
ENV NEXT_PRIVATE_STANDALONE true
WORKDIR /app
COPY --from=deps /app/node_modules ./node_modules
COPY ../frontend ./
RUN npm run build

# 3. Production image, copy all the files and run next
FROM base AS runner
WORKDIR /app

ENV NODE_ENV=production

RUN addgroup -g 1001 -S nodejs
RUN adduser -S nextjs -u 1001

# Copy the necessary files from the builder stage
COPY --from=builder /app/public ./public
COPY --from=builder --chown=nextjs:nodejs /app/.next/standalone ./
COPY --from=builder --chown=nextjs:nodejs /app/.next/static ./.next/static
COPY --from=builder --chown=nextjs:nodejs /app/package.json ./

USER nextjs

EXPOSE 3000

ENV PORT 3000
HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 CMD wget -qO- http://localhost:3000/health || exit 1

# Run the Next.js app
CMD ["npm", "start"]
