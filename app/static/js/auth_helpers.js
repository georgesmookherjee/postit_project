// function isConnected() {
//     return fetch("/auth/status")
//         .then(res => {
//             if (!res.ok) return false;
//             return res.json().then(data => data.logged_in);
//         })
//         .catch(() => false);
// }

// // Utilisation avant les requêtes
// isConnected().then(connect => {
//     if (connect) {
//         // Faire la requête API
//     } else {
//         showNotification("Veuillez vous connecter");
//         // Rediriger vers la page de connexion si nécessaire
//         window.location.href = "/";
//     }
// });