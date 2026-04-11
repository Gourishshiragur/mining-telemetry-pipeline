#!/bin/bash

# Exit if any command fails
set -e

echo "🚀 Starting Databricks Deployment..."

# Set environment (dev/prod)
ENV=${1:-dev}

echo "Environment: $ENV"

# Validate bundle config
echo "🔍 Validating bundle..."
databricks bundle validate

# Deploy to workspace
echo "📦 Deploying bundle..."
databricks bundle deploy --target $ENV

# Run job (optional)
echo "▶️ Running job..."
databricks bundle run mining_pipeline_job --target $ENV

echo "✅ Deployment Completed Successfully!"