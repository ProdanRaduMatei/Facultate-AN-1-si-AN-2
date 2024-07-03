package repository;

import domain.Identifiable;

public interface IRepository<ID, T extends Identifiable<ID>> {

    /**
     * Adds the given element to the repository
     * @param element
     * @return Returns the added element or null object if it could not be added
     */
    T add(T element);
    /**
     * Removes the given element from the repository
     * @param id
     * @return Returns the element or null object if it could not be found
     */
    T delete(ID id);

    /**
     * Updates the element in the repository having the given id with the new given element
     * @param id
     * @param newElement
     * @return Returns the old element or null object if it could not be found. If the old element was not found, the
     * repo will not be modified
     */
    T update(ID id, T newElement);

    /**
     * Gets the element having the given id in the repo
     * @param id
     * @return The found element or null object if it does not exist
     */
    T findById(ID id);

    /**
     * 
     * @return
     */
    Iterable<T> getAll();

    int size();
}
