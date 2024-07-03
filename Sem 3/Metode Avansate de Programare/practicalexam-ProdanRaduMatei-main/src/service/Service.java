package service;

import repository.Repository;

public class Service {
    private Repository repo;

    public Service(Repository repo) {
        this.repo = repo;
    }
}
