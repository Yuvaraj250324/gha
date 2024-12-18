const core = require('@actions/core');
const exec = require('@actions/exec');

async function run() {
  try {
    const nodeVersion = core.getInput('node-version');
    await exec.exec(`nvm install ${nodeVersion}`);
    await exec.exec('npm install');
  } catch (error) {
    core.setFailed(error.message);
  }
}

run();