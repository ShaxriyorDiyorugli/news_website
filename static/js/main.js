// Page loading animation
document.addEventListener('DOMContentLoaded', function() {
    console.log('NewsWebsite loaded successfully');

    // Add fade-in animation to cards
    const cards = document.querySelectorAll('.news-card');
    cards.forEach((card, index) => {
        card.style.opacity = '0';
        card.style.transform = 'translateY(20px)';
        setTimeout(() => {
            card.style.transition = 'all 0.5s ease';
            card.style.opacity = '1';
            card.style.transform = 'translateY(0)';
        }, index * 100);
    });
});

// Search functionality (optional)
function searchNews() {
    const searchTerm = document.getElementById('searchInput').value.toLowerCase();
    const newsCards = document.querySelectorAll('.news-card');

    newsCards.forEach(card => {
        const title = card.querySelector('.card-title').textContent.toLowerCase();
        const content = card.querySelector('.card-text').textContent.toLowerCase();

        if (title.includes(searchTerm) || content.includes(searchTerm)) {
            card.style.display = 'block';
        } else {
            card.style.display = 'none';
        }
    });
}

// Back to top button
window.onscroll = function() {
    const btn = document.getElementById('backToTop');
    if (btn) {
        if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
            btn.style.display = 'block';
        } else {
            btn.style.display = 'none';
        }
    }
};

function topFunction() {
    document.body.scrollTop = 0;
    document.documentElement.scrollTop = 0;
}