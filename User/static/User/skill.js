const skillsInput = document.getElementById('skillsInput');
const skillsContainer = document.getElementById('skillsContainer');


        // Listen for input changes
    skillsInput.addEventListener('input', updateSkills);
    function updateSkills() {
        const skills = skillsInput.value.trim();
        if (skills) {
            // Split skills by comma (you can adjust this based on your input format)
            const skillList = skills.split(',');
            // Clear existing skills
            skillsContainer.innerHTML = '';
            // Add each skill as a chip
            skillList.forEach(skill => {
                const skillChip = document.createElement('div');
                skillChip.classList.add('skill-chip');
                skillChip.innerHTML = `
                    <span>${skill}</span>
                    <span class="cancel-icon" onclick="removeSkill(this)">❌</span>
                `;
                skillsContainer.appendChild(skillChip);
            });
        }
    }
    // Function to remove a skill
    function removeSkill(element) {
        const skillChip = element.closest('.skill-chip');
        skillChip.remove();
        skillsInput.value = "";
    }
