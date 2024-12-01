function deleteUser(userId) {
    fetch(`/users/${userId}`, {
        method: 'DELETE',
        headers: {
            'Content-Type': 'application/json',
        },
    })
    .then(response => {
        if (response.ok) {
            location.reload(); // Atualiza a página ou redireciona
        } else {
            alert('Erro ao deletar usuário.');
        }
    });
}