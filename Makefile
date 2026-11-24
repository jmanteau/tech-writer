.DEFAULT_GOAL := help
.PHONY: help py-setup quality test vale-sync

RESET := \033[0m
CYAN := \033[36m
BLUE := \033[0;34m
GREEN := \033[0;32m
YELLOW := \033[0;33m

##@ Help
help: ## Display this help message
	@awk 'BEGIN {FS = ":.*##"; printf "Usage:\n  make $(YELLOW)<target>$(RESET)\n"} /^[a-zA-Z_0-9-]+:.*?##/ { printf "  $(CYAN)%-20s$(RESET) %s\n", $$1, $$2 } /^##@/ { printf "\n$(GREEN)%s$(RESET)\n", substr($$0, 5) } ' $(MAKEFILE_LIST)

##@ Setup
py-setup: ## Setup Python development environment
	uv --native-tls venv
	uv --native-tls sync --group dev

vale-sync: ## Download the Vale packages (Google, vale-ai-tells)
	cd vale && vale sync

##@ Code Quality
quality: ## Run all quality checks (ruff + mypy)
	@echo "$(BLUE)Running ruff linter...$(RESET)"
	uv --native-tls run ruff check .
	@echo "$(BLUE)Running ruff format check...$(RESET)"
	uv --native-tls run ruff format --check .
	@echo "$(BLUE)Running mypy...$(RESET)"
	uv --native-tls run mypy tests
	@echo "$(GREEN)[OK] All quality checks passed$(RESET)"

##@ Testing
test: ## Run tests
	@echo "$(BLUE)Running tests...$(RESET)"
	uv --native-tls run pytest
	@echo "$(GREEN)[OK] Tests complete$(RESET)"
