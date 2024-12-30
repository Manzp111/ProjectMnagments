function openEditModal(id, name, address, type, rent) {
        // Open the modal
        document.getElementById('editModal').style.display = 'block';

        // Set values in the modal
        document.getElementById('property_id').value = id;
        document.getElementById('property_name').value = name;
        document.getElementById('property_address').value = address;
        document.getElementById('property_type').value = type;
        document.getElementById('property_rent').value = rent;

        // Update the form's action attribute with the correct ID
        const form = document.querySelector('#editModal form');
        form.action = `/property/edit/${id}/`; // Update to match your URL pattern
    }
