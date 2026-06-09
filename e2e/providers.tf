terraform {
  backend "local" {
    path = "state/e2e.tfstate"
  }
}
