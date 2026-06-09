#!/bin/bash
set -e

SCENARIO=$1
WORKSPACE_DIR=$(pwd)
PLAN_OUTPUT="${WORKSPACE_DIR}/scenarios/${SCENARIO}/${SCENARIO}.tfplan"
STATE_FILE="${WORKSPACE_DIR}/state/e2e.tfstate"
STATE_DIR="$(dirname "$STATE_FILE")"

# Create state directory if it doesn't exist
mkdir -p "$STATE_DIR"

# Initialize baseline state from main directory if not already done
if [ ! -f "$STATE_FILE" ]; then
  echo "Creating baseline state from main e2e directory..."
  terraform init -upgrade
  terraform apply -auto-approve
fi

# Navigate to scenario directory
cd "scenarios/${SCENARIO}"

# Initialize scenario with shared backend pointing to baseline state
terraform init -upgrade

# Generate plan showing changes relative to baseline state
terraform plan -out "${PLAN_OUTPUT}"

# Return to workspace
cd "$WORKSPACE_DIR"

